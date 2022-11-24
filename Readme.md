# Poc export data FastAPI

Para rodar o projeto você precisa estar na versão `3.10`do python
<br>
**Também é necessário estar com a VPN ativada**


### Dependencias
```bash
pip install -r requirements.txt
```

## Execute o projeto

```bash
uvicorn main:app --reload --port 5000
```

# Testando

Para testar acesse `http://localhost:5000` <br>
Em seguida cofira a pasta `/out` na raiz do projeto <br>
Ela deverá ter um novo arquivo csv pra cada chamada feita na api
