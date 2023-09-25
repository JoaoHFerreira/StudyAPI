TESTANDOOOOOOOOOOOOOOOOOOOOOOOOOO

# API
Api for studies purposes

# Fetch Journals News
The key goals of this project are:
* Daily fetch Globo news (scraping notions);
* Store the news in a database (PostgreSQL);
* Provide an API to access the news (REST API);
* Provide a web interface to access the news (ReactJS).
* Provide date filters to access the news (REST API and ReactJS);
* Provide a search field to access the news provider (REST API and ReactJS);

# Database Modeling
## Globo Case URL pattern
https://g1.globo.com/fantastico/noticia/YEAR/MONTH/DAY/NOTICE-NAME-SPLITED-BY-.ghtml

Certainly! Here's an updated schema with descriptions for the columns in each table:

1. **News**
    - `id` (Primary Key): Unique identifier for each news article.
    - `title`: The title of the news article.
    - `description`: A brief description or summary of the article.
    - `url`: The URL of the news article.
    - `date`: The date when the news article was published.
    - `created_at`: Timestamp when the news article record was created.
    - `updated_at`: Timestamp when the news article record was last updated.
    - `provider_id` (Foreign Key): References the `News Provider` table to identify the news provider.
    - `category_id` (Foreign Key): References the `News Category` table to identify the news category.
    - `author_id` (Foreign Key): References the `News Author` table to identify the news author.

2. **News Provider**
    - `id` (Primary Key): Unique identifier for each news provider.
    - `name`: The name of the news provider.
    - `url`: The URL of the news provider's website.
    - `created_at`: Timestamp when the news provider record was created.
    - `updated_at`: Timestamp when the news provider record was last updated.

3. **News Category**
    - `id` (Primary Key): Unique identifier for each news category.
    - `name`: The name of the news category.
    - `created_at`: Timestamp when the news category record was created.
    - `updated_at`: Timestamp when the news category record was last updated.

4. **News Author**
    - `id` (Primary Key): Unique identifier for each news author.
    - `name`: The name of the news author.
    - `created_at`: Timestamp when the news author record was created.
    - `updated_at`: Timestamp when the news author record was last updated.

5. **News Tag**
    - `id` (Primary Key): Unique identifier for each news tag.
    - `name`: The name of the news tag.
    - `created_at`: Timestamp when the news tag record was created.
    - `updated_at`: Timestamp when the news tag record was last updated.

# Next Steps:
* Create database using SQLAlchemy ORM;
* Create a REST API using FastAPI;
    * Create a route to fetch news;
    * Create a route to fetch news by date;
    * Create a route to fetch news by provider;
    * Create a route to fetch news by category;
    * Create a route to fetch news by author;
    * Create a route to fetch news by tag;
    * Create unit tests;
* Split code into modules;
* Create a CI/CD pipeline using GitHub Actions;
* Create a web interface using ReactJS;
* Create a Dockerfile to run the FastAPI application;
* Create a Dockerfile to run the ReactJS application;
* Create a docker-compose file to run the FastAPI and ReactJS applications;
* Create a Kubernetes deployment to run the FastAPI and ReactJS applications Locally using minikube;
* Create a Kubernetes deployment to run the FastAPI and ReactJS applications in the cloud using AWS EKS;
