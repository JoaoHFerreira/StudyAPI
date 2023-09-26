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