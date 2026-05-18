# algoritmos gulosos e backtracking - soluções

repositório com as soluções dos exercícios de **backtracking** da disciplina:

- [7-algoritmos-gulosos-e-backtracking](https://github.com/PUCRS-Poli-ES-ALAV/7-algoritmos-gulosos-e-backtracking) (pucrs)

**link para entrega:** https://github.com/bengo501/Backtracking

---

## texto sugerido para o fórum

> segue o link do repositório com as soluções em backtracking dos problemas das **n-rainhas** e da **soma dos subconjuntos** (primeira solução e todas as soluções), incluindo análise de complexidade e tabelas com contagem de iterações, instruções e tempo de execução:
>
> https://github.com/bengo501/Backtracking

---

## estrutura

| arquivo | descrição |
|---------|-----------|
| `nrainhas.py` | n-rainhas: `resolver_um` e `resolver_todas` |
| `soma_subconjuntos.py` | soma zero: `soma_zero_um` e `soma_zero_todos` |
| `benchmark.py` | gera tabelas de medição (iterações, instruções, tempo) |

## como executar

```bash
python nrainhas.py
python soma_subconjuntos.py
python benchmark.py
```

### contagem de iterações e instruções

- **iteração:** cada chamada recursiva à função `backtrack`
- **instrução:** operações elementares contabilizadas no backtracking (comparações, tentativas de coluna/elemento)

---

## análise de complexidade

### n-rainhas

| método | tempo | espaço | observação |
|--------|-------|--------|------------|
| `resolver_um` | **o(n!)** pior caso | **o(n)** | para na primeira solução; poda por colunas inválidas |
| `resolver_todas` | **o(n!)** | **o(n · s)** | explora toda a árvore; s = número de soluções |

### soma dos subconjuntos (soma zero)

| método | tempo | espaço | observação |
|--------|-------|--------|------------|
| `soma_zero_um` | **o(2^n)** pior caso | **o(n)** | melhor caso: para na primeira solução |
| `soma_zero_todos` | **o(2^n)** | **o(n + s·n)** | percorre todos os ramos; s = quantidade de soluções |

---

## tabelas de resultados (backtracking)

valores obtidos com `python benchmark.py` (máquina local; tempo pode variar).

### n-rainhas – primeira solução (`resolver_um`)

| n | soluções | iterações | instruções | tempo (s) |
|---|----------|-----------|------------|-----------|
| 4 | 1 | 9 | 107 | 0.000032 |
| 6 | 1 | 32 | 913 | 0.000200 |
| 8 | 1 | 114 | 5866 | 0.000847 |
| 10 | 1 | 103 | 7422 | 0.000857 |
| 12 | 1 | 262 | 26838 | 0.003250 |

### n-rainhas – todas as soluções (`resolver_todas`)

| n | soluções | iterações | instruções | tempo (s) |
|---|----------|-----------|------------|-----------|
| 4 | 2 | 17 | 245 | 0.000046 |
| 6 | 4 | 153 | 5079 | 0.000630 |
| 7 | 40 | 552 | 22730 | 0.002861 |
| 8 | 92 | 2057 | 111281 | 0.014965 |

### soma zero – primeira solução (`soma_zero_um`)

**exemplos do enunciado:**

| entrada | soluções | iterações | instruções | tempo (s) |
|---------|----------|-----------|------------|-----------|
| `{-7,-3,-2,5,8}` | 1 | 36 | 55 | 0.000030 |
| `{1,2,3,4,5,10}` | 0 | 127 | 190 | 0.000063 |
| `{-5,2,3,-1,1}` | 1 | 4 | 7 | 0.000003 |

**|conjunto| variável (par 42/-42 no início):**

| n | soluções | iterações | instruções | tempo (s) |
|---|----------|-----------|------------|-----------|
| 10 | 1 | 3 | 5 | 0.000003 |
| 20 | 1 | 3 | 5 | 0.000003 |
| 50 | 1 | 3 | 5 | 0.000002 |
| 100 | 1 | 3 | 5 | 0.000002 |
| 500 | 1 | 3 | 5 | 0.000004 |

**pior caso (só positivos, sem solução):**

| n | soluções | iterações | instruções | tempo (s) |
|---|----------|-----------|------------|-----------|
| 10 | 0 | 2047 | 3070 | 0.000622 |
| 15 | 0 | 65535 | 98302 | 0.020726 |
| 18 | 0 | 524287 | 786430 | 0.396084 |
| 20 | 0 | 2097151 | 3145726 | 0.960402 |

### soma zero – todas as soluções (`soma_zero_todos`)

**exemplos do enunciado:**

| entrada | soluções | iterações | instruções | tempo (s) |
|---------|----------|-----------|------------|-----------|
| `{-7,-3,-2,5,8}` | 1 | 63 | 94 | 0.000046 |
| `{1,2,3,4,5,10}` | 0 | 127 | 190 | 0.000044 |
| `{-5,2,3,-1,1}` | 3 | 63 | 94 | 0.000026 |

**|conjunto| variável:**

| n | soluções | iterações | instruções | tempo (s) |
|---|----------|-----------|------------|-----------|
| 8 | 2 | 511 | 766 | 0.000182 |
| 10 | 2 | 2047 | 3070 | 0.000663 |
| 12 | 10 | 8191 | 12286 | 0.004653 |
| 15 | 68 | 65535 | 98302 | 0.035452 |
| 18 | 526 | 524287 | 786430 | 0.260591 |

---

## conclusões das medições

1. **n-rainhas:** `resolver_todas` cresce muito mais que `resolver_um` porque explora toda a árvore (ex.: n=8 → 92 soluções, 2057 iterações).
2. **soma zero:** com solução fácil no início, `soma_zero_um` é quase constante; no pior caso (sem solução) as iterações seguem ~2^n (ex.: n=20 → 2.097.151 iterações).
3. **soma_zero_todos** torna-se impraticável para n grande; para n=18 já são 524.287 iterações e 526 soluções.

---

## referência

enunciado original: [PUCRS - algoritmos gulosos e backtracking](https://github.com/PUCRS-Poli-ES-ALAV/7-algoritmos-gulosos-e-backtracking#o-problema-1)
