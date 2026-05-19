from __future__ import annotations

import sys
from dataclasses import dataclass


@dataclass
class metricas:
    iteracoes: int = 0  #conta chamadas do backtrack
    instrucoes: int = 0  #conta operações básicas

    def zerar(self) -> None:
        self.iteracoes = 0
        self.instrucoes = 0


def _ajustar_limite_recursao(n: int) -> None:
    necessario = n + 100
    if sys.getrecursionlimit() < necessario:
        sys.setrecursionlimit(necessario)  #evita erro com conjuntos grandes


def soma_zero_um(conjunto: list[int], m: metricas | None = None) -> list[int] | None:
    _ajustar_limite_recursao(len(conjunto))
    escolhidos: list[int] = []

    def backtrack(indice: int, soma: int) -> bool:
        if m:
            m.iteracoes += 1
            m.instrucoes += 1
        if soma == 0 and escolhidos:  #achou subconjunto válido
            return True
        if indice == len(conjunto):  #fim da lista
            return False

        elemento = conjunto[indice]
        if m:
            m.instrucoes += 1

        escolhidos.append(elemento)  #inclui elemento
        if backtrack(indice + 1, soma + elemento):
            return True
        escolhidos.pop()  #backtrack

        if backtrack(indice + 1, soma):  #não inclui elemento
            return True
        return False

    if backtrack(0, 0):
        return escolhidos[:]
    return None


def soma_zero_todos(conjunto: list[int], m: metricas | None = None) -> list[list[int]]:
    _ajustar_limite_recursao(len(conjunto))
    resultados: list[list[int]] = []
    escolhidos: list[int] = []
    vistos: set[tuple[int, ...]] = set()  #evita repetir o mesmo subconjunto

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
        backtrack(indice + 1, soma)  #explora incluir e não incluir

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
