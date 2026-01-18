# SQLAlchemy Async Fundamentals

**Short description:**
My first junior-level backend project demonstrating correct usage of SQLAlchemy 2.0 async ORM, clean project structure, and explicit async database interaction patterns.
Designed as a foundational portfolio project focused purely on database layer skills.

## Table of Contents
- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running](#running)
- [Database Models](#database-models)
- [CRUD Operations](#crud-operations)
- [Async Patterns Used](#async-patterns-used)
- [Raw SQL](#raw-sql)
- [Debugging](#debugging)
- [Requirements](#requirements)
- [License](#license)

## Overview
`SQLAlchemy Async Fundamentals` features:

- CRUD functions for creating, retrieving, updating, and deleting users
- CRUD functions for creating posts linked to specific users
- Bidirectional one-to-many relationship between users and posts
- Eager loading of posts with `selectinload`
- Async ORM models using `SQLAlchemy 2.0`
- `Pydantic` schemas for data validation and output serialization
- Explicit async session management (`AsyncSession`, `async with`)
- Raw SQL queries executed asynchronously (`text`)
- Step-by-step demo script showing table creation, user/post operations, and cleanup

## Tech Stack
- Language: `Python 3.12+`
- Database / ORM: `PostgreSQL`, `SQLAlchemy 2.0 (async)`
- Driver: `asyncpg`
- Data validation / schemas: `Pydantic`

![Python](https://img.shields.io/badge/python-3.12+-blue)
![SQLAlchemy](https://img.shields.io/badge/sqlalchemy-2.0-orange)
![PostgreSQL](https://img.shields.io/badge/postgresql-15-blue)

## Project Structure
```
sqlalchemy-async-fundamentals/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── core_queries.py
│   ├── crud/
│   │   ├── __init__.py
│   │   ├── users.py
│   │   └── posts.py
│   └── utils/
│       ├── __init__.py
│       └── loaders.py
├── requirements.txt
├── README.md
└── LICENSE
```

## Installation
1. Clone repository:  
```
git clone <repo_url>
cd sqlalchemy-async-fundamentals
```
2. Create virtual environment:  
- Linux / macOS: `python -m venv venv && source venv/bin/activate`  
- Windows PowerShell: `python -m venv venv; venv\Scripts\Activate.ps1`  
- Windows CMD: `python -m venv venv && venv\Scripts\activate.bat`  
3. Install dependencies: `pip install -r requirements.txt`  
4. Ensure `PostgreSQL` is running and update credentials in `config.py`

## Running
Run the demo script: `python app/main.py`  
What happens: tables are created, a user is inserted, a post is created, user with posts is queried, user age is updated, and user is deleted.

## Database Models
- `User`: id (PK `Integer`), name (`String`), age (`Integer`), posts (one-to-many relationship)  
- `Post`: id (PK `Integer`), title (`String`), content (`Text`), user_id (foreign key → `users.id`)  
- Relationship: bidirectional with `back_populates`, cascade delete enabled

## CRUD Operations
- Users: create user, get user by id, get user with posts (eager loaded), update user age, delete user  
- Posts: create post for a specific user  
- All operations use `AsyncSession`, explicit commits, and explicit `refresh` where needed

## Async Patterns Used
- `create_async_engine`, `async_sessionmaker`  
- `async with AsyncSessionLocal()`  
- `await session.execute(...)`, `await session.commit()`, `await session.refresh(...)`  
No synchronous `SQLAlchemy` usage is present

## Raw SQL
Example raw SQL execution: `SELECT COUNT(*) FROM users`  
Executed via `sqlalchemy.text` and async session execution. Demonstrates mixing ORM and raw SQL safely

## Debugging
- `SQLAlchemy` `echo=True` enabled  
- All SQL queries printed to console  
- Clear session boundaries for easier tracing  
- Simple structure to inspect behavior step-by-step

## Requirements
`requirements.txt`:  
- `sqlalchemy>=2.0`  
- `asyncpg>=0.29`  
- `pydantic>=2.0`

## License
`MIT License`
