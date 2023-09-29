# Connecting To The Database
Install psql
```bash
sudo apt install postgresql postgresql-contrib
```

# Up the docker compose
```bash
docker-compose up -d
```
# Connect to the database
```bash
psql -h localhost -p  5432  -U admin -d news_fetcher_db
```

# Shutdown the docker compose
```bash
docker-compose down
```


# Fazer recursão na pagina de noticias
* Se pagina de noticias tem mais noticias, fazer recursão se não salvar noticias;
* Se tiver ambos, primeiro salvar notícias e depois fazer recursão;
* Pra cada página de notícias, salvar o link da notícia;

Ex de recursão, enquanto não chega 10 soma +1
```python
def recursion(n):
    if n == 10:
        return n
    else:
        return recursion(n+1)
```