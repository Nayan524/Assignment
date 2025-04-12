# Web Scraper Project

This project scrapes quotes from quotes.toscrape.com and saves them to MongoDB using Docker.

## Setup
1. Install Docker from https://www.docker.com/get-started.
2. Clone this project: `https://github.com/Nayan524/Assignment.git`.
3. Go to the project folder: `cd Assignment/Assignment`.

## Running
1. Start everything: `docker-compose up --build`.
   - This builds and runs Scrapy and MongoDB.
2. To check saved quotes:
   - Run: `docker exec -it mongodb mongosh -u user -p assignment`
   - Type: `use scrapy_db` then `db.quotes.find().pretty()`
3. Stop: `docker-compose down`.

## Settings
- **MongoDB**: Uses username `user` and password `assignment`.
- **Environment Variables**:
  - `MONGO_URI`: Set in `docker-compose.yaml` (default: `mongodb://admin:password@mongodb:27017/`).
  - `MONGO_DB`: Database name (default: `scrapy_db`).
- Change these in `docker-compose.yaml` if needed.

## Tools Used
- Docker
- Python 3.9 (in container)
- Scrapy and PyMongo (see `requirements.txt`)