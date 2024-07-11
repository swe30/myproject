# Django Project for Login, Registration, and Profile Management

## Requirements

- Python 3.8+
- Django 4.0+
- PostgreSQL
- Redis or RabbitMQ (for Celery)
- Virtualenv

## Setup Instructions

### 1. Create and Activate Virtual Environment

```bash
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
pip install -r requirements.txt


#Configure PostgreSQL

CREATE DATABASE myprojectdb;
CREATE USER myprojectuser WITH PASSWORD 'password';
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE myprojectdb TO myprojectuser;

#Apply Migrations
python manage.py migrate

#Run Redis Server
redis-server
#Run the Development Server
python manage.py runserver






