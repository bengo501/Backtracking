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

def _ajustar_limite_recursao(n: int) -> None: #ajusta o limite de recursão
    necessario = n + 100
    if sys.getrecursionlimit() < necessario:
        sys.setrecursionlimit(necessario)  #evita erro com conjuntos grandes

def soma_zero_um(conjunto: list[int], m: metricas | None = None) -> list[int] | None:
    _ajustar_limite_recursao(len(conjunto)) #ajusta o limite de recursão
    escolhidos: list[int] = []

    def backtrack(indice: int, soma: int) -> bool: #backtracking para encontrar a primeira solução
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

    if backtrack(0, 0): #encontrou uma solução
        return escolhidos[:]
    return None

def soma_zero_todos(conjunto: list[int], m: metricas | None = None) -> list[list[int]]: #resolve o problema da soma zero para todas as soluções
    _ajustar_limite_recursao(len(conjunto)) #ajusta o limite de recursão
    resultados: list[list[int]] = []
    escolhidos: list[int] = []
    vistos: set[tuple[int, ...]] = set()  #evita repetir o mesmo subconjunto

    def backtrack(indice: int, soma: int) -> None: #backtracking para encontrar todas as soluções   
        if m: #mede o tempo de execução
            m.iteracoes += 1
            m.instrucoes += 1
        if soma == 0 and escolhidos: #achou subconjunto válido
            chave = tuple(sorted(escolhidos))
            if chave not in vistos: #evita repetir o mesmo subconjunto
                vistos.add(chave)
                resultados.append(escolhidos.copy())

        if indice == len(conjunto): #fim da lista
            return

        elemento = conjunto[indice]
        if m: #mede o tempo de execução
            m.instrucoes += 1

        escolhidos.append(elemento)
        backtrack(indice + 1, soma + elemento) #explora incluir e não incluir
        escolhidos.pop()
        backtrack(indice + 1, soma)  #explora incluir e não incluir

    backtrack(0, 0) #encontrou todas as soluções
    return resultados #retorna todas as soluções

def formatar_conjunto(valores: list[int]) -> str: #formata o conjunto para exibição
    return "{" + ", ".join(str(v) for v in valores) + "}"

def main() -> None: #função principal
    casos = [  #exemplos do enunciado
        [-7, -3, -2, 5, 8],
        [1, 2, 3, 4, 5, 10],
        [-5, 2, 3, -1, 1],
    ]

    print("=== soma zero: primeira solução ===\n")
    for conjunto in casos:
        m = metricas() #mede o tempo de execução
        sub = soma_zero_um(conjunto, m) #primeira solução
        print(f"entrada: {formatar_conjunto(conjunto)}")
        print(f"solucao: {formatar_conjunto(sub) if sub else 'nenhuma'}")
        print(f"iteracoes: {m.iteracoes} | instrucoes: {m.instrucoes}\n")
    print("=== soma zero: todas as soluções ===\n")
    for conjunto in casos: #exemplos do enunciado
        m = metricas() #mede o tempo de execução
        sols = soma_zero_todos(conjunto, m) #todas as soluções
        print(f"entrada: {formatar_conjunto(conjunto)}")
        print(f"total: {len(sols)} | iteracoes: {m.iteracoes} | instrucoes: {m.instrucoes}")
        for i, sub in enumerate(sols, start=1):
            print(f"  {i}. {formatar_conjunto(sub)}")
        print()

if __name__ == "__main__":
    main()
