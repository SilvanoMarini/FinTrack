# FinTrack API

Personal finance API built with Django REST Framework, following Clean Architecture principles and SOLID design.

## About

FinTrack is a personal finance micro-SaaS that allows users to record transactions, categorize expenses, view monthly summaries, and set budget alerts.

Built as a portfolio project covering:

- Clean Architecture with clear layer separation
- SOLID principles applied in practice
- RESTful API with JWT authentication
- Two-language stack (Python/Django + Go)
- Docker containerization with docker-compose
- CI/CD with GitHub Actions
- AWS deployment

## Tech Stack

- **Python 3.12** + **Django 5.1** + **Django REST Framework**
- **PostgreSQL** (production) / SQLite (development)
- **JWT** authentication via `djangorestframework-simplejwt`
- **Go** — notifications and budget alert microservice
- **Docker** + **docker-compose**
- **GitHub Actions** for CI/CD
- **AWS** (ECS + RDS + S3)

## Architecture

The project follows Clean Architecture with 4 well-defined layers:

```
fintrack/
├── domain/             # Pure business rules and entities (zero Django)
│   ├── entities/       # Transaction, Category, Budget
│   ├── repositories/   # Repository interfaces (ABCs)
│   └── exceptions/     # Domain exceptions
│
├── use_cases/          # Use cases — business rule orchestration
│   ├── create_transaction.py
│   ├── get_monthly_summary.py
│   └── set_budget_alert.py
│
├── infrastructure/     # Concrete implementations (Django ORM, external)
│   ├── django/         # Models and repository implementations
│   └── external/       # Notifications client (Go service)
│
└── interfaces/         # Views, Serializers, URLs
    └── api/
```

**Core rule:** dependencies always point inward. The `domain/` layer imports nothing from Django — it can be reused in any Python framework.

## Features

- [x] Base structure with Clean Architecture
- [ ] JWT authentication (register and login)
- [ ] Transaction CRUD (income and expenses)
- [ ] User-defined categories
- [ ] Financial summary by period
- [ ] Budget alerts by category
- [ ] Notifications microservice (Go)
- [ ] Docker containerization
- [ ] CI/CD pipeline
- [ ] AWS deployment

## Running Locally

### Requirements

- Python 3.12+
- [uv](https://github.com/astral-sh/uv)

### Setup

```bash
# Clone the repository
git clone https://github.com/SilvanoMarini/FinTrack.git
cd FinTrack

# Install dependencies
uv sync

# Configure environment variables
cp .env.example .env
# edit .env with your settings

# Run migrations
uv run python manage.py migrate

# Start the server
uv run python manage.py runserver
```

### Environment Variables

Create a `.env` file at the project root based on `.env.example`:

```
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

### Tests

```bash
uv run pytest
```

### Lint

```bash
uv run ruff check .
```

## SOLID in Practice

**Single Responsibility** — each class and function has one responsibility. The `CreateTransaction` use case only creates transactions; it does not serialize or save directly.

**Open/Closed** — new notification types or repositories are added without modifying existing code.

**Dependency Inversion** — use cases depend on interfaces (`ABC`), not on concrete Django ORM implementations.

## License

MIT
