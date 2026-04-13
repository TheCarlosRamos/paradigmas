# Lista de Exercícios - Forth

Leia os exercícios em [exercicios.md](exercicios.md) e
[exercicios-array.md](exercicios-array.md) e implemente as funcionalidades
descritas lá nos arquivos `exercicios.fs` e `exercicios-array.fs`.


## Testes

Use o próprio forth para testar suas implementações localmente. Depois, confira
se os testes automatizados estão passando usando `pytest`:

```bash
pytest tests/ -v
```

Existem várias opções no pytest que permitem rodar apenas um teste específico,
ou um grupo de testes, apenas os que falharam na última execução, etc. Consulte
a documentação do pytest para mais detalhes. Seguem alguns exemplos mais comuns:


```bash
# Rodar apenas um teste específico (filtra por nome):
pytest -k pop_at -v

# Rodar apenas testes que falharam na última execução:
pytest --lf

# Limita número de testes erros
pytest --maxfail=1
```



