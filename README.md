# backtracking - entrega

**repositório:** https://github.com/bengo501/Backtracking

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
| n-rainhas | o(n!) | o(n!) |
| soma zero | o(2^n) | o(2^n) |

iteração = cada chamada do `backtrack`  
instrução = comparações e tentativas contadas no código

as tabelas completas saem ao rodar `python benchmark.py`.

## fórum (copiar e colar)

> soluções em backtracking: n-rainhas e soma dos subconjuntos, com complexidade e medições.
> https://github.com/bengo501/Backtracking
