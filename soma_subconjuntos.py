"""
problema da soma dos subconjuntos (soma zero) - backtracking.
uma solução (soma_zero_um) e todas (soma_zero_todos).
"""

from __future__ import annotations

import sys
from dataclasses import dataclass


@dataclass
class metricas:
    iteracoes: int = 0
    instrucoes: int = 0

    def zerar(self) -> None:
        self.iteracoes = 0
        self.instrucoes = 0


def _ajustar_limite_recursao(n: int) -> None:
    necessario = n + 100
    if sys.getrecursionlimit() < necessario:
        sys.setrecursionlimit(necessario)


def soma_zero_um(conjunto: list[int], m: metricas | None = None) -> list[int] | None:
    _ajustar_limite_recursao(len(conjunto))
    escolhidos: list[int] = []

    def backtrack(indice: int, soma: int) -> bool:
        if m:
            m.iteracoes += 1
            m.instrucoes += 1
        if soma == 0 and escolhidos:
            return True
        if indice == len(conjunto):
            return False

        elemento = conjunto[indice]
        if m:
            m.instrucoes += 1

        escolhidos.append(elemento)
        if backtrack(indice + 1, soma + elemento):
            return True
        escolhidos.pop()

        if backtrack(indice + 1, soma):
            return True
        return False

    if backtrack(0, 0):
        return escolhidos[:]
    return None


def soma_zero_todos(conjunto: list[int], m: metricas | None = None) -> list[list[int]]:
    _ajustar_limite_recursao(len(conjunto))
    resultados: list[list[int]] = []
    escolhidos: list[int] = []
    vistos: set[tuple[int, ...]] = set()

    def backtrack(indice: int, soma: int) -> None:
        if m:
            m.iteracoes += 1
            m.instrucoes += 1
        if soma == 0 and escolhidos:
            chave = tuple(sorted(escolhidos))
            if chave not in vistos:
                vistos.add(chave)
                resultados.append(escolhidos.copy())

        if indice == len(conjunto):
            return

        elemento = conjunto[indice]
        if m:
            m.instrucoes += 1

        escolhidos.append(elemento)
        backtrack(indice + 1, soma + elemento)
        escolhidos.pop()
        backtrack(indice + 1, soma)

    backtrack(0, 0)
    return resultados


def formatar_conjunto(valores: list[int]) -> str:
    return "{" + ", ".join(str(v) for v in valores) + "}"


def main() -> None:
    conjunto = [-7, -3, -2, 5, 8]
    m = metricas()
    sub = soma_zero_um(conjunto, m)
    print(f"entrada: {formatar_conjunto(conjunto)}")
    print(f"solucao: {formatar_conjunto(sub) if sub else 'nenhuma'}")
    print(f"iteracoes: {m.iteracoes} | instrucoes: {m.instrucoes}")


if __name__ == "__main__":
    main()
