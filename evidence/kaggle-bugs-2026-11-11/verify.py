"""Recompute reported outcomes from the distributed receipts and fingerprints.

Author: Aridio Silva, Independent Researcher, ORCID 0009-0008-2411-6995.
Copyright 2026 Aridio Silva. SPDX-License-Identifier: Apache-2.0
Created and last updated: 2026-11-11, America/Sao_Paulo.
"""
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from statistics import NormalDist

HERE = Path(__file__).resolve().parent
ROUND_ORDER = ('R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'S54M')
EXPECTED_RUNS = (2, 1, 6, 26, 15, 5, 54)
EXPECTED_RESOLUTIONS = (0, 0, 1, 13, 3, 0, 20)
MEMBER_NAMES = {
    'evaluation.json', 'official-verdict-before-identity.json', 'canonical-collection.json',
    'tests.log', 'captured.patch', 'memory-guard-event.json',
}
SHA256 = re.compile(r'[0-9a-f]{64}')

def read_json(filename):
    return json.loads((HERE / filename).read_text(encoding='utf-8'))

def verify_manifest():
    listed = set()
    for line in (HERE / 'manifest.sha256').read_text(encoding='ascii').splitlines():
        expected, name = line.split('  ', 1)
        assert name not in listed and '/' not in name and '\\' not in name, name
        assert hashlib.sha256((HERE / name).read_bytes()).hexdigest() == expected, name
        listed.add(name)
    assert listed == {p.name for p in HERE.iterdir() if p.is_file() and p.name != 'manifest.sha256'}

def classify(row):
    if row['reported_class'] == 'R':
        assert row['patch_applied'] is True and row['patch_bytes'] > 0
        assert row['test_execution_confirmed'] is True and row['test_exit_code'] == 0
        assert all(row[k] is True for k in ('resolved_summary','resolved_evaluation','resolved_verdict'))
        assert {'captured.patch', 'evaluation.json', 'official-verdict-before-identity.json'} <= set(
            row['source_member_sha256'],
        )
        return 'R'
    if (row['patch_applied'] is True and row['patch_bytes'] and row['test_execution_confirmed'] is True
            and row['test_exit_code'] == 1):
        required = set(row['required_sha256'])
        if not required:
            return 'C2'
        return 'C2a' if required.intersection(row['failure_sha256']) else 'C2b'
    if row['reported_class'] in {'CONTEXTO_ESGOTADO', 'SAIDA_TRUNCADA'}:
        return 'C4'
    return 'C3' if row['reported_class'] == 'INCONCLUSIVO' or row['patch_bytes'] else 'C5'

def wilson_interval(successes, total):
    z = NormalDist().inv_cdf(0.975)
    rate = successes / total
    scale = 1 + z * z / total
    center = (rate + z * z / (2 * total)) / scale
    half_width = z * (rate * (1 - rate) / total + z * z / (4 * total**2))**0.5 / scale
    return 100 * (center - half_width), 100 * (center + half_width)

def count_outcomes(rows):
    return Counter(classify(row) for row in rows)

def main():
    verify_manifest()
    with (HERE / 'inventory.csv').open(encoding='utf-8', newline='') as handle:
        inventory = list(csv.DictReader(handle))
    data = (HERE / 'executions.jsonl').read_text(encoding='utf-8')
    rows = [json.loads(line) for line in data.splitlines()]
    indexed_inventory = {row['task']: row for row in inventory}
    expected_deferred = [row['task'] for row in inventory if row['deferred'] == 'True']
    assert len(inventory) == len(indexed_inventory) == 87 and len(expected_deferred) == 1
    assert Counter(row['cohort'] for row in inventory) == {'R1-R6':33,'S54M':54}
    assert all(row['deferred'] in {'True','False'} for row in inventory)
    assert len({row['task_id_sha256'] for row in inventory}) == 87
    assert all(SHA256.fullmatch(row['task_id_sha256']) for row in inventory)
    assert len(rows) == len({(row['round'],row['task']) for row in rows}) == 109
    assert tuple(Counter(row['round'] for row in rows)[tag] for tag in ROUND_ORDER) == EXPECTED_RUNS
    assert len({row['task'] for row in rows}) == 86
    assert set(indexed_inventory) - {row['task'] for row in rows} == set(expected_deferred)
    for row in rows:
        tag = row['round']
        assert indexed_inventory[row['task']]['cohort'] == ('S54M' if tag == 'S54M' else 'R1-R6')
        source_members = row['source_member_sha256']
        assert set(source_members) <= MEMBER_NAMES
        for digests in (source_members.values(), row['required_sha256'], row['failure_sha256']):
            assert all(SHA256.fullmatch(digest) for digest in digests)
    archive_rows = read_json('source-archives.json')['rounds']
    assert tuple(row['round'] for row in archive_rows) == ROUND_ORDER
    assert tuple(row['executions'] for row in archive_rows) == EXPECTED_RUNS
    assert all(SHA256.fullmatch(row[key]) for row in archive_rows for key in ('archive_sha256','summary_sha256'))

    historical = sorted(
        (row for row in rows if row['round'] != 'S54M'),
        key=lambda row: ROUND_ORDER.index(row['round']),
    )
    first, latest = {}, {}
    for row in historical:
        first.setdefault(row['task'], row)
        latest[row['task']] = row
    assert sum(classify(row) == 'R' for row in first.values()) == 14
    assert sum(n > 1 for n in Counter(row['task'] for row in historical).values()) == 16
    assert count_outcomes(latest.values()) == {'R':17, 'C2a':13, 'C2':1, 'C5':1}
    assert count_outcomes(historical) == {'R':17, 'C2a':25, 'C2b':2, 'C2':4, 'C5':7}
    s54m = [row for row in rows if row['round'] == 'S54M']
    assert count_outcomes(s54m) == {'R':20, 'C2a':23, 'C2b':7, 'C3':3, 'C4':1}
    assert all(row['model_request_limit'] == 30 for row in s54m)
    assert sum(row['patch_only_reproduction_or_probe'] is True for row in s54m if classify(row) != 'R') == 13
    repositories = Counter(
        indexed_inventory[row['task']]['repository'] for row in s54m if classify(row) == 'R'
    )
    assert repositories == {'fastapi':12,'rich':7,'requests':1}
    totals = count_outcomes([*latest.values(), *s54m])
    assert totals == {'R':37, 'C2a':36, 'C2b':7, 'C2':1, 'C3':3, 'C4':1, 'C5':1}
    assert tuple(sum(classify(row) == 'R' for row in rows if row['round'] == tag) for tag in ROUND_ORDER) == EXPECTED_RESOLUTIONS

    ops = read_json('operations.json')
    assert ops['all_processed'] is True and ops['scheduled'] == 54
    assert ops['cleanup_confirmed'] is True and ops['automatic_retry_performed'] is False
    assert round(ops['cell_events']['CELL_END']['elapsed_seconds']) == 20082
    assert set(ops['cell_events']) == {'CELL_START','CELL_END'}
    by_task = {row['task']:row for row in s54m}
    guards = ops['memory_guard_events']
    assert len(guards) == len({event['task'] for event in guards}) == 2
    for event in guards:
        row = by_task[event['task']]
        assert classify(row) == 'C3' and event['exceeded'] is True and event['tree_gone'] is True
        assert event['peak_rss_bytes'] >= event['threshold_bytes']
        assert event['source_member_sha256'] == row['source_member_sha256']['memory-guard-event.json']
    assert sum(row['evaluation_syntax_error'] for row in s54m if classify(row) == 'C3') == 1
    assert sum(row['patch_bytes'] == 0 for row in s54m if classify(row) == 'C4') == 1
    lo, hi = wilson_interval(20, 54)
    assert (round(lo,1),round(hi,1)) == (25.4,50.4)
    print('PASS: 87 selected; 86 executed; 109 executions across seven rounds.')
    print(f'37 resolved; {100*37/87:.1f}% of selected. Unresolved: 49; patch rejected: 44; required-test failure: 36.')
    print(f'S54M: 20/54 ({100*20/54:.1f}%); 95% Wilson interval {lo:.1f}% to {hi:.1f}%.')
    print('S54M: 30 rejected (23 required failures, 7 outside); two recorded memory-guard interventions.')
    print('Integrity and arithmetic checked on publication extracts. Private ZIPs and experiments were not replayed.')

if __name__ == '__main__':
    main()
