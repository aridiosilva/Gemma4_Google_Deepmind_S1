from collections import deque
from itertools import product

TERMINAIS = {"ACEITO", "ABSTENCAO"}
PESO = {"pronto": 0, "propor": 3, "verificar": 2, "publicar": 1}


def transicoes(estado, mutante):
    r, b, fase = estado
    if fase == "pronto" and (r == 0 or b < 4):
        yield "sem_reserva", (r, b, "ABSTENCAO")
    elif fase == "pronto":
        yield "iniciar", (r - 1, b - 1, "propor")
    elif fase == "propor":
        yield "patch", (r, b - 1, "verificar")
        for evento in ("sem_patch", "timeout_propor"):
            yield evento, (r, b - 1, "pronto")
    elif fase == "verificar":
        yield "prova_vinculada", (r, b - 1, "publicar")
        for evento in ("falsa", "trocada", "timeout_verificar"):
            destino = "publicar" if mutante and evento == "falsa" else "pronto"
            yield evento, (r, b - 1, destino)
    elif fase == "publicar":
        yield "commit_ok", (r, b - 1, "ACEITO")
        yield "commit_falhou", (r, b - 1, "pronto")


def verificar(mutante=False):
    fila = deque()
    for r, b in product(range(11), range(13)):
        fila.append(((r, b, "pronto"), False, ()))
    vistos = set()
    arestas = 0
    while fila:
        estado, prova, trilha = fila.popleft()
        if (estado, prova) in vistos:
            continue
        vistos.add((estado, prova))
        r, b, fase = estado
        assert 0 <= r <= 10 and 0 <= b <= 12
        if fase == "ACEITO" and not prova:
            return trilha
        proximos = list(transicoes(estado, mutante))
        assert bool(proximos) == (fase not in TERMINAIS)
        for evento, proximo in proximos:
            rr, bb, ff = proximo
            assert 0 <= bb <= b and 0 <= rr <= r
            if ff not in TERMINAIS:
                assert 4 * rr + PESO[ff] < 4 * r + PESO[fase]
            prova_nova = evento == "prova_vinculada" or (
                prova and evento == "commit_ok"
            )
            arestas += 1
            fila.append((proximo, prova_nova, trilha + (evento,)))
    return len(vistos), arestas


print("controle:", verificar())
print("mutante:", " -> ".join(verificar(mutante=True)))
