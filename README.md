# backtracking - entrega

https://github.com/bengo501/Backtracking

## arquivos

- `nrainhas.py` — n-rainhas (uma solução e todas)
- `soma_subconjuntos.py` — soma zero (uma solução e todas)
- `benchmark.py` — mede iterações, instruções e tempo

## como rodar

```bash
python nrainhas.py
python soma_subconjuntos.py
python benchmark.py
```

## complexidade

| problema | uma solução | todas |
|----------|-------------|-------|
| n-rainhas | o(n!) tempo, o(n) espaço | o(n!) tempo, o(n·s) espaço |
| soma zero | o(2^n) tempo, o(n) espaço | o(2^n) tempo, o(n+s·n) espaço |

- iteração = cada chamada do `backtrack`
- instrução = comparações e tentativas contadas no código

## resultados dos exemplos

### n-rainhas — primeira solução

| n | soluções | iterações | instruções | tempo (s) |
|---|----------|-----------|------------|-----------|
| 4 | 1 | 9 | 107 | 0.000057 |
| 6 | 1 | 32 | 913 | 0.000240 |
| 8 | 1 | 114 | 5866 | 0.001280 |
| 10 | 1 | 103 | 7422 | 0.001358 |
| 12 | 1 | 262 | 26838 | 0.003339 |

### n-rainhas — todas as soluções

| n | soluções | iterações | instruções | tempo (s) |
|---|----------|-----------|------------|-----------|
| 4 | 2 | 17 | 245 | 0.000050 |
| 6 | 4 | 153 | 5079 | 0.000687 |
| 7 | 40 | 552 | 22730 | 0.003076 |
| 8 | 92 | 2057 | 111281 | 0.018103 |

### soma zero — primeira solução

| entrada | soluções | iterações | instruções | tempo (s) |
|---------|----------|-----------|------------|-----------|
| {-7,-3,-2,5,8} | 1 | 36 | 55 | 0.000046 |
| {1,2,3,4,5,10} | 0 | 127 | 190 | 0.000079 |
| {-5,2,3,-1,1} | 1 | 4 | 7 | 0.000005 |

### soma zero — todas as soluções

| entrada | soluções | iterações | instruções | tempo (s) |
|---------|----------|-----------|------------|-----------|
| {-7,-3,-2,5,8} | 1 | 63 | 94 | 0.000055 |
| {1,2,3,4,5,10} | 0 | 127 | 190 | 0.000078 |
| {-5,2,3,-1,1} | 3 | 63 | 94 | 0.000047 |

### soma zero — conjuntos grandes (só 1ª solução)

| tamanho | iterações | instruções | tempo (s) |
|---------|-----------|------------|-----------|
| 50 | 3 | 5 | 0.000003 |
| 100 | 3 | 5 | 0.000003 |
| 500 | 3 | 5 | 0.000003 |
| 1000 | 3 | 5 | 0.000004 |

valores com par 42/-42 no início (solução rápida). rode `python benchmark.py` para gerar de novo.

## fórum

> soluções em backtracking: n-rainhas e soma dos subconjuntos, com complexidade e medições.
> https://github.com/bengo501/Backtracking
