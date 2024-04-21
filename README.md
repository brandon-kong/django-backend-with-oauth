# Django Backend with OAuth

This is a Django backend with OAuth authentication. It uses the Django Rest Framework to create a REST API. The OAuth authentication is done using the `dj-rest-auth` package.

This template is designed for applications using a SPA (Single Page Application) frontend. The frontend is expected to handle the OAuth flow and send the access token to the backend. The backend will then use the access token to authenticate the user.

## Features

- User creation/login/logout/reset password
- Creating client applications for OAuth
- OAuth authentication

## Setup

1. Clone the repository
2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

or on Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install the dependencies

```bash
pip install -r requirements.txt
```

4. Run the migrations

```bash
python manage.py migrate
```

5. Create a superuser

```bash
python manage.py createsuperuser
```

6. Run the server

```bash
python manage.py runserver
```

Additionally, there is a docker-compose file that can be used to run the backend, the PostgreSQL database, and a Redis server for caching. To use it, run:

```bash
docker-compose up
```

## Usage

The API endpoints are available at `http://localhost:8000/api/v1/`. The admin panel is available at `http://localhost:8000/admin/`, and the dj-rest-auth endpoints are available at `http://localhost:8000/auth/`.