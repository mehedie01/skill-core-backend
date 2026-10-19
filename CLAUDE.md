# CLAUDE.md - Skill Core Solution

## Architecture
- **Backend:** Django 5 + DRF, PostgreSQL. Located in `/skill-core-backend`.
- **Frontend:** React 18 + Vite, deployed on Vercel. Located in `/skill-core-solution`.
- **API Base:** `/api/` (e.g., `/api/services/`).

## Folder Map
- Backend: `api/models.py`, `api/views.py`, `api/serializers.py`.
- Frontend: `src/pages/`, `src/components/`, `src/api/endpoints.js`.

## Conventions
- Use functional components with hooks (React).
- Use Django REST Framework class-based views where possible.
- Environment variables via `django-decouple` and `import.meta.env`.

## How to Run Tests
- Backend: `python manage.py test`
- Frontend: `npm run test` (if configured).