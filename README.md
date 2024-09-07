# Todo App Backend

This is a Django-based backend for a simple Todo application. It provides a RESTful API for managing todo items and user authentication.

## Features

- CRUD operations for todo items
- User registration and authentication
- Token-based authentication for API access
- Filtered todo items by user

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/todo-app-backend.git
   cd todo-app-backend
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser (optional):
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

The API will be available at `http://localhost:8000/api/`.

## API Endpoints

### Authentication

- `POST /api/register/`: Register a new user
  - Request body: `{"username": "newuser", "password": "newpass", "email": "new@user.com"}`
  - Response: `{"username": "newuser", "email": "new@user.com"}`

- `POST /api/login/`: Login and receive an authentication token
  - Request body: `{"username": "newuser", "password": "newpass"}`
  - Response: `{"token": "your-auth-token", "user_id": 1, "username": "newuser"}`

### Todo Items

All todo endpoints require authentication. Include the token in the Authorization header: `Authorization: Token your-auth-token`

- `GET /api/todos/`: List all todos for the authenticated user
- `POST /api/todos/`: Create a new todo
  - Request body: `{"title": "New Todo", "description": "Description", "due_date": "2023-12-31", "status": false}`
- `GET /api/todos/{id}/`: Retrieve a specific todo
- `PUT /api/todos/{id}/