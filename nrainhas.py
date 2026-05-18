"""
problema das n-rainhas - backtracking.
uma solução (resolver_um) e todas as soluções (resolver_todas).
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class metricas:
    iteracoes: int = 0
    instrucoes: int = 0

    def zerar(self) -> None:
        self.iteracoes = 0
        self.instrucoes = 0


def coluna_segura(
    tabuleiro: list[int], linha: int, coluna: int, m: metricas | None = None
) -> bool:
    for i in range(linha):
        if m:
            m.instrucoes += 2
        if tabuleiro[i] == coluna:
            return False
        if abs(tabuleiro[i] - coluna) == abs(i - linha):
            return False
    return True


def resolver_um(n: int, m: metricas | None = None) -> list[int] | None:
    """primeira solução válida; tabuleiro[i] = coluna na linha i."""
    tabuleiro = [-1] * n

    def backtrack(linha: int) -> bool:
        if m:
            m.iteracoes += 1
            m.instrucoes += 1
        if linha == n:
            return True
        for coluna in range(n):
            if m:
                m.instrucoes += 1
            if coluna_segura(tabuleiro, linha, coluna, m):
                tabuleiro[linha] = coluna
                if backtrack(linha + 1):
                    return True
                tabuleiro[linha] = -1
        return False

    if backtrack(0):
        return tabuleiro
    return None


def resolver_todas(n: int, m: metricas | None = None) -> list[list[int]]:
    """todas as soluções válidas."""
    solucoes: list[list[int]] = []
    tabuleiro = [-1] * n

    def backtrack(linha: int) -> None:
        if m:
            m.iteracoes += 1
            m.instrucoes += 1
        if linha == n:
            solucoes.append(tabuleiro.copy())
            return
        for coluna in range(n):
            if m:
                m.instrucoes += 1
            if coluna_segura(tabuleiro, linha, coluna, m):
                tabuleiro[linha] = coluna
                backtrack(linha + 1)
                tabuleiro[linha] = -1

    backtrack(0)
    return solucoes


def formatar_tabuleiro(tabuleiro: list[int]) -> str:
    n = len(tabuleiro)
    linhas = []
    for i in range(n):
        linha = ["."] * n
        linha[tabuleiro[i]] = "q"
        linhas.append(" ".join(linha))
    return "\n".join(linhas)


def main() -> None:
    try:
        n = int(input("informe n (n >= 2): ").strip())
    except ValueError:
        print("entrada inválida.")
        return
    if n < 2:
        print("n deve ser >= 2.")
        return

    m = metricas()
    solucoes = resolver_todas(n, m)
    print(f"total: {len(solucoes)} | iteracoes: {m.iteracoes} | instrucoes: {m.instrucoes}")
    if solucoes:
        print(formatar_tabuleiro(solucoes[0]))


if __name__ == "__main__":
    main()
