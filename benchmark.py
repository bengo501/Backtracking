from __future__ import annotations

import random
import time

from nrainhas import metricas as metricas_rainhas
from nrainhas import resolver_todas, resolver_um
from soma_subconjuntos import metricas as metricas_soma
from soma_subconjuntos import soma_zero_todos, soma_zero_um


def medir_rainhas_um(n: int) -> dict:
    m = metricas_rainhas()
    t0 = time.perf_counter()
    sol = resolver_um(n, m)  #primeira solução
    tempo = time.perf_counter() - t0
    return {
        "n": n,
        "solucoes": 1 if sol else 0,
        "iteracoes": m.iteracoes,
        "instrucoes": m.instrucoes,
        "tempo_s": tempo,
    }


def medir_rainhas_todas(n: int) -> dict:
    m = metricas_rainhas()
    t0 = time.perf_counter()
    sols = resolver_todas(n, m)  #todas as soluções
    tempo = time.perf_counter() - t0
    return {
        "n": n,
        "solucoes": len(sols),
        "iteracoes": m.iteracoes,
        "instrucoes": m.instrucoes,
        "tempo_s": tempo,
    }


def medir_soma_um(conjunto: list[int]) -> dict:
    m = metricas_soma()
    t0 = time.perf_counter()
    sol = soma_zero_um(conjunto, m)
    tempo = time.perf_counter() - t0
    return {
        "n": len(conjunto),
        "solucoes": 1 if sol else 0,
        "iteracoes": m.iteracoes,
        "instrucoes": m.instrucoes,
        "tempo_s": tempo,
    }


def medir_soma_todos(conjunto: list[int]) -> dict:
    m = metricas_soma()
    t0 = time.perf_counter()
    sols = soma_zero_todos(conjunto, m)
    tempo = time.perf_counter() - t0
    return {
        "n": len(conjunto),
        "solucoes": len(sols),
        "iteracoes": m.iteracoes,
        "instrucoes": m.instrucoes,
        "tempo_s": tempo,
    }


def gerar_aleatorio(tamanho: int) -> list[int]:
    random.seed(42)
    if tamanho < 2:
        return [1, -1][:tamanho]
    restante = [random.randint(-100, 100) for _ in range(tamanho - 2)]
    return [42, -42] + restante  #par oposto facilita achar solução rápida


def gerar_sem_solucao(tamanho: int) -> list[int]:
    random.seed(42)
    return [random.randint(1, 100) for _ in range(tamanho)]  #só positivos


def linha_md(r: dict) -> str:
    return (
        f"| {r['n']} | {r['solucoes']} | {r['iteracoes']} | "
        f"{r['instrucoes']} | {r['tempo_s']:.6f} |"
    )


def cabecalho() -> str:
    return "| n | soluções | iterações | instruções | tempo (s) |\n|---|----------|-----------|------------|-----------|"


def main() -> None:
    print("# resultados do benchmark\n")

    print("## n-rainhas - primeira solução\n")
    print(cabecalho())
    for n in [4, 6, 8, 10, 12]:
        print(linha_md(medir_rainhas_um(n)))

    print("\n## n-rainhas - todas as soluções\n")
    print(cabecalho())
    for n in [4, 6, 7, 8]:
        print(linha_md(medir_rainhas_todas(n)))

    print("\n## soma zero - primeira solução\n")
    print(cabecalho())
    casos = [[-7, -3, -2, 5, 8], [1, 2, 3, 4, 5, 10], [-5, 2, 3, -1, 1]]
    for c in casos:
        r = medir_soma_um(c)
        print(f"| `{c}` | {r['solucoes']} | {r['iteracoes']} | {r['instrucoes']} | {r['tempo_s']:.6f} |")

    print("\n## soma zero - todas as soluções\n")
    print(cabecalho())
    for c in casos:
        r = medir_soma_todos(c)
        print(f"| `{c}` | {r['solucoes']} | {r['iteracoes']} | {r['instrucoes']} | {r['tempo_s']:.6f} |")


if __name__ == "__main__":
    main()
