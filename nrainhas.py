from __future__ import annotations
from dataclasses import dataclass
@dataclass
class metricas: #classe para medir o tempo de execução
    iteracoes: int = 0  #conta chamadas do backtrack
    instrucoes: int = 0  #conta operações básicas
    def zerar(self) -> None:
        self.iteracoes = 0
        self.instrucoes = 0

def coluna_segura( #verifica se a coluna é segura
    tabuleiro: list[int], linha: int, coluna: int, m: metricas | None = None #tabuleiro: lista de colunas, linha: linha atual, coluna: coluna atual, m: métricas
) -> bool:
    for i in range(linha):
        if m:
            m.instrucoes += 2  #duas comparações por rainha anterior
        if tabuleiro[i] == coluna:  #mesma coluna
            return False
        if abs(tabuleiro[i] - coluna) == abs(i - linha):  #mesma diagonal
            return False
    return True

def resolver_um(n: int, m: metricas | None = None) -> list[int] | None: #resolve o problema das n-rainhas para uma solução
    tabuleiro = [-1] * n  #tabuleiro[i] = coluna da rainha na linha i

    def backtrack(linha: int) -> bool: #backtracking para encontrar a primeira solução
        if m:
            m.iteracoes += 1
            m.instrucoes += 1
        if linha == n:  #todas as linhas preenchidas
            return True
        for coluna in range(n):
            if m:
                m.instrucoes += 1
            if coluna_segura(tabuleiro, linha, coluna, m):
                tabuleiro[linha] = coluna
                if backtrack(linha + 1):  #próxima linha
                    return True  #para na primeira solução
                tabuleiro[linha] = -1  #backtrack
        return False

    if backtrack(0): #encontrou uma solução
        return tabuleiro
    return None

def resolver_todas(n: int, m: metricas | None = None) -> list[list[int]]: #resolve o problema das n-rainhas para todas as soluções
    solucoes: list[list[int]] = []
    tabuleiro = [-1] * n
    def backtrack(linha: int) -> None: #backtracking para encontrar todas as soluções
        if m:
            m.iteracoes += 1
            m.instrucoes += 1
        if linha == n:
            solucoes.append(tabuleiro.copy())  #salva solução e continua
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

def formatar_tabuleiro(tabuleiro: list[int]) -> str: #formata o tabuleiro para exibição
    n = len(tabuleiro)
    linhas = []
    for i in range(n):
        linha = ["."] * n
        linha[tabuleiro[i]] = "q"
        linhas.append(" ".join(linha))
    return "\n".join(linhas)

def main() -> None: #função principal   
    valores_n = [4, 6, 7, 8]  #casos de teste automáticos
    print("=== n-rainhas: primeira solução ===\n")
    for n in valores_n:
        m = metricas()
        sol = resolver_um(n, m) 
        print(f"n = {n}")
        if sol:
            print(f"colunas (1-based): {[c + 1 for c in sol]}")
            print(formatar_tabuleiro(sol)) #exibe o tabuleiro
        else:
            print("sem solução")
        print(f"iteracoes: {m.iteracoes} | instrucoes: {m.instrucoes}\n")
    print("=== n-rainhas: todas as soluções ===\n")
    for n in valores_n:
        m = metricas()
        sols = resolver_todas(n, m)
        print(f"n = {n} | total: {len(sols)} | iteracoes: {m.iteracoes} | instrucoes: {m.instrucoes}")
        for i, sol in enumerate(sols, start=1):
            print(f"  solução {i}: {[c + 1 for c in sol]}")
        print()

if __name__ == "__main__":
    main()