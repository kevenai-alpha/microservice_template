# Database Submodule

## Overview
The `generic_microservice_database` submodule is responsible for managing database interactions within the KEVEN microservice architecture. It provides database models, connection handling, migrations, and query abstractions to ensure efficient and maintainable data operations.

## Features
- **Database Connection Management**: Handles connections to PostgreSQL, Redis, or other databases as configured.
- **ORM Support**: Uses SQLAlchemy or other ORM libraries to interact with relational databases.
- **Migration Support**: Utilizes Alembic or a similar tool to manage schema changes.
- **Caching**: Integrates with Redis for high-speed caching where necessary.
- **Configuration via Environment Variables**: Uses `.env` or OS environment variables for database credentials and settings.

## Installation
Ensure that the `generic_microservice_database` submodule is included as a dependency in your microservice's `pyproject.toml`:

```toml
[tool.poetry.dependencies]
generic_microservice_database = { version = "0.1.0", source = "local-pypi" }
```

Run the following command to install the dependency:
```bash
poetry install
```

## Environment Variables
The following environment variables should be configured for database connectivity:

| Variable            | Description |
|---------------------|-------------|
| `DATABASE_URL`      | Connection string for the primary database |
| `REDIS_URL`        | Connection string for Redis (if used) |
| `DB_POOL_SIZE`     | Maximum database connection pool size |

Example `.env` file:
```ini
DATABASE_URL=postgresql://user:password@localhost:5432/mydb
REDIS_URL=redis://localhost:6379/0
DB_POOL_SIZE=10
```

## Usage
### Connecting to the Database
Example of initializing a database session with SQLAlchemy:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
```

### Running Migrations
If using Alembic, apply migrations with:
```bash
alembic upgrade head
```

## Contributing
- Follow the project's contribution guidelines.
- Use pre-commit hooks for code formatting and linting.
- Ensure all database schema changes are versioned properly using migrations.

## License
This submodule is licensed under **AGPL-3.0**.
