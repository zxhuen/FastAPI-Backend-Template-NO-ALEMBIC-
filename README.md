# FastAPI + Supabase Template

## Setup

### 1. Create virtual environment

python -m venv venv
source venv/bin/activate # or venv\Scripts\activate

### 2. Install dependencies

pip install -r requirements.txt

### 3. Change .env file

DATABASE_URL= dawshboard > connect > ORM > copy the pooler and remove "?pgbouncer=true"
SUPABASE_URL= go to your supabase dashboard and you'll find Project URL
SUPABASE_KEY= project settings > api keys > Legacy anon, service_role API keys

### 4. Run Server

python -m uvicorn app.main:app --reload
http://127.0.0.1:8000/docs (docs)

### Purpose

This repository was created as a reusable backend template while learning production-oriented FastAPI development. It serves as the starting point for future projects and will continue to evolve as new features and best practices are added.
