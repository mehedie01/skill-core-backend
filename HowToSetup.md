# How to Setup Skill Core Solution

## Prerequisites
- Python 3.10+, Node.js 18+, PostgreSQL 14+
- Git, Docker (for Docker setup)

## Setup Target 1: Local VPS / Machine

### Backend (Django)
1. `git clone <your-repo-url>`
2. `cd skill-core-backend`
3. `python -m venv venv && source venv/bin/activate`
4. `pip install -r requirements.txt`
5. Copy `.env.example` to `.env` and fill values.
6. `python manage.py migrate`
7. `python manage.py createsuperuser`
8. `python manage.py runserver`

### Frontend (React + Vite)
1. `cd ../skill-core-solution`
2. `npm install`
3. Copy `.env.example` to `.env` and set `VITE_API_URL=http://127.0.0.1:8000/api`
4. `npm run dev`

### First Admin Login
- URL: `http://127.0.0.1:8000/admin/`
- Use the superuser credentials created in step 7.

## Setup Target 2: Docker Compose
1. Ensure Docker Desktop is running.
2. From project root, run `docker-compose up --build`
3. Backend runs on `:8000`, Frontend on `:5173`.
4. Run `docker-compose exec backend python manage.py migrate` and `createsuperuser`.

## Database Setup
- The app uses PostgreSQL. Ensure `DATABASE_URL` is set in `.env`.
- Migrations are automatically applied via `python manage.py migrate`.