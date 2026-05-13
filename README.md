# TaskFlow — Enterprise TODO Application

Enterprise-grade task management with AI-powered workflows, built with Next.js 14 + FastAPI + PostgreSQL.

## Quick Start

```bash
# 1. Copy environment template
cp .env.example .env
# Fill in your values

# 2. Start everything with Docker Compose
docker compose up

# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# API docs: http://localhost:8000/docs
```

## Development (without Docker)

**Backend:**
```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
alembic upgrade head
uvicorn main:app --reload
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

## Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Next.js 14 (App Router, TypeScript) |
| Styling | Tailwind CSS — Neo-Brutalism design |
| Backend | FastAPI (Python 3.12, PEP 8) |
| Database | PostgreSQL 16 + SQLAlchemy 2 + Alembic |
| Auth | JWT + OAuth 2.0 (Google) |
| AI | LangChain + OpenAI/Anthropic |
| Deployment | Vercel (frontend) + Neon (Postgres) |

## Jira Tickets

Project: [TODO APP](https://konfigai.atlassian.net/jira/core/projects/TODO/board)

| Ticket | Feature |
|--------|---------|
| TODO-25 | Project Scaffolding (this PR) |
| TODO-26 | Authentication & Authorization |
| TODO-27 | Task Management CRUD API |
| TODO-28 | Task Views UI (List + Kanban) |
| TODO-29 | Categorization & Metadata |
| TODO-30 | Search & Filtering |
| TODO-31 | AI Task Breakdown |
| TODO-32 | Smart Auto-Categorization |
| TODO-33 | Agentic Workflows |
| TODO-34 | Testing, QA & CI/CD |
