"""Integrity and receipt-consistency check; no scientific execution.
Aridio Silva, Independent Researcher, ORCID 0009-0008-2411-6995.
Copyright 2026 Aridio Silva. SPDX-License-Identifier: Apache-2.0
Created/updated 2026-11-07 America/Sao_Paulo.
"""
from pathlib import Path
from collections import Counter
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parent
def read(name):return json.loads((ROOT/'evidence'/name).read_text(encoding='utf-8'))
def data(name):return read(name)['data']
def main():
 lines=(ROOT/'MANIFEST.sha256').read_text(encoding='ascii').splitlines()
 paths=set()
 for line in lines:
  digest,name=line.split('  ',1)
  p=ROOT/name
  assert p.resolve().is_relative_to(ROOT.resolve()) and p.is_file(),name
  assert hashlib.sha256(p.read_bytes()).hexdigest()==digest,name
  paths.add(name)
 assert paths=={p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file() and p.name!='MANIFEST.sha256' and '.git' not in p.parts},'Unlisted or missing file'
 sources=read('source-catalog.json')['sources'];ids={x['id'] for x in sources}
 assert len(ids)==len(sources)
 for p in (ROOT/'evidence').glob('*.json'):
  obj=json.loads(p.read_text(encoding='utf-8'))
  if 'source_id' in obj:assert obj['source_id'] in ids,p.name
 for p in ROOT.rglob('*.md'):
  for target in re.findall(r'\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
   if not re.match(r'https?://',target):assert (p.parent/target).is_file(),(p.name,target)
 pilot=read('pilot-receipts.json');assert pilot['manifest_files_verified']==266
 for arm,tokens in [('B',14881),('P',16268)]:
  a=pilot['arms'][arm]
  assert a['audit']['actual_tokens']==tokens and a['audit']['model_requests']==6
  assert a['resolved'] and a['evaluation']['resolved'] and a['patch_bytes']==214
 assert pilot['arms']['B']['patch_sha256']==pilot['arms']['P']['patch_sha256']
 cases=data('task16-junit.json')['cases'];assert len(cases)==52
 assert Counter(x['outcome'] for x in cases)['skipped']==3
 assert data('task16-verdict.json')['resolved'] is False
 w=read('w18-synthetic-receipt.json');assert len(w['cases'])==9
 assert sum(c['original']['accepted'] and not c['proposal']['accepted'] for c in w['cases'])==w['incorrect_acceptances_reproduced']==3
 parser=read('parser-forum-receipt.json')
 for name in ['array_bare_close_746336','args_json_quotes_bracket_753973','args_code_in_array_745138']:
  assert not parser['stock'][name]['returned'] and parser['compat'][name]['returned']
  assert parser['compat'][name]['raised']=='MalformedGemma4ToolCall'
 real=data('v12-real-worker.json')
 assert real['audit']['model_requests']==18 and real['tokens']==324628
 assert real['patch_bytes']==1095 and real['patch_applied'] and not real['resolved']
 assert real['test_exit_code']==1 and not real['automatic_retry_performed']
 junit=data('v12-junit-identities.json')
 assert junit['counts']=={'passed':55,'failure':1}
 required={x['name']:x['outcome'] for x in junit['cases'] if x['name'] in ['test_zwj','test_non_printable']}
 assert required=={'test_zwj':'passed','test_non_printable':'failure'}
 stop=real['preventive_stops'][0]
 assert not stop['backend_request_sent'] and stop['input_tokens']+stop['template_margin']+stop['output_min_tokens']>real['audit']['limits']['context_tokens']
 trace=data('v12-trace-metadata.json')
 nonempty=[x for x in trace['steps'] if x['source']=='agent' and x['has_nonempty_message']]
 assert len(nonempty)==21 and sum(x['event_type']=='thinking' for x in nonempty)==17
 assert trace['final_metrics']['total_tokens']==real['tokens']
 for name,tests in [('v12-unit-local.json',73),('v12r1-unit-local.json',88)]:
  d=data(name);assert d['identity']=='LOCAL_TEST_ONLY' and d['tests_run']==tests
  assert d['errors']==d['failures']==d['skipped']==d['model_calls']==d['scientific_tasks_started']==0
 for name in ['v12-k2-local.json','v12r1-k2-local.json']:
  d=data(name);assert d['identity']=='LOCAL_TEST_ONLY' and d['model_calls_real']==d['scientific_tasks_started']==0 and not d['kaggle_started']
  assert len(d['checks'])==124 and all(v is True for v in d['checks'].values())
  assert d['batch_final']['resolved']==d['batch_final']['started']==32 and d['batch_final']['denominator']==33
 rows=[json.loads(x) for x in (ROOT/'evidence/v12-progress-events.jsonl').read_text(encoding='utf-8').splitlines()]
 index=data('v12-progress-index.json');assert len(rows)==index['progress_records']==840
 assert dict(Counter(x['event'] for x in rows))==index['event_counts']
 assert index['event_counts']['EM_ANDAMENTO']==187 and index['event_counts']['SUPERVISAO_ATIVA']==153
 a=read('archive-audit.json');assert a['v12_real']['manifest_members_verified']==1538 and a['v12_real']['mismatches']==0
 assert a['v12r1_local']['pair_is_byte_identical_inside_final']
 print(f'PASS: {len(paths)} distributed files; receipt arithmetic and classifications consistent. Originals and full harness were not rerun.')
if __name__=='__main__':main()
