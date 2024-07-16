# py-clean-architecture

This is the strongest CleanArchitecture implementation I could think of in Python's DDD.

## Language & FW & Library & Tool

- Language is [Python3.12](https://docs.python.org/3.12/).
  - package installer is [uv](https://github.com/astral-sh/uv).
  - package manager is [rye](https://github.com/astral-sh/rye).
  - linter and formatter is [ruff](https://github.com/astral-sh/ruff).
- FW is [FastAPI](https://fastapi.tiangolo.com).
- Database is [MySQL](https://www.mysql.com/).
  - MySQL client library is [PyMySQL](https://github.com/PyMySQL/PyMySQL).
  - SQL toolkit and ORM is [SQLAlchemy](https://www.sqlalchemy.org/).
- Containerization is [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/).
  - Python image is [python:3.12-slim](https://github.com/docker-library/python/blob/5ed2758efb58d9acaafa90515caa43edbcfe4c4e/3.12/slim-bookworm/Dockerfile).
  - MySQL image is [mysql:8.0](https://github.com/docker-library/mysql/blob/db7daba00da79773c594b94bd91c9deeca1c9c88/8.0/Dockerfile.oracle).

## Structure

Underlying idea is [The Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html).

Layers
- domain layer means Entities.
- application layer means Use Cases.
- adapter layer means Interface Adapters.
- infrastructure layer means Frameworks and Drivers.

```
src/py_clean_architecture
├── domain
│   ├── entity
│   ├── repository
│   ├── service
│   └── error.py
├── application
│   ├── input
│   ├── output
│   ├── presenter
│   ├── unit_of_work
│   └── usecase
├── adapter
│   ├── controller
│   ├── gateway
│   │   ├── repository
│   │   └── unit_of_work
│   └── presenter
├── infrastructure
│   ├── database
│   │   ├── model
│   │   └── setting.py
│   ├── di
│   ├── request
│   ├── response
│   └── router
├── config.py
└── main.py
```
