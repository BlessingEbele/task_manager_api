# Task Management API

A Django-based API for managing tasks, allowing users to create, update, delete, and mark tasks as complete or incomplete. This project is designed to simplify task management with a clean and functional API.

## Features
- User Authentication (registration, login, logout)
- CRUD operations for tasks
- Mark tasks as complete or incomplete
- Search tasks by title or description
- API documentation with Django REST Framework (Browsable API)

## API Endpoints
| Endpoint                  | Method | Description                   |
|---------------------------|--------|-------------------------------|
| `/api/register/`          | POST   | Register a new user           |
| `/api/login/`             | POST   | Login for an existing user    |
| `/api/tasks/`             | GET    | List all tasks for a user     |
| `/api/tasks/`             | POST   | Create a new task             |
| `/api/tasks/<id>/`        | GET    | Retrieve a single task        |
| `/api/tasks/<id>/`        | PUT    | Update a task                 |
| `/api/tasks/<id>/`        | DELETE | Delete a task                 |
| `/api/tasks/search/?q=`   | GET    | Search tasks by keyword       |

## Technology Stack
- **Backend Framework**: Django
- **API Framework**: Django REST Framework
- **Database**: SQLite (Development)
- **Deployment**: PythonAnywhere

## Installation and Setup

### Prerequisites
- Python 3.8 or later
- pip (Python package manager)
- Git (Version control)

### Local Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/task_manager_api.git
   cd task_manager_api
