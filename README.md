# ToDo-FastApi-ReactJS

## About project

Simple ToDo application with user registration, login and adding of "To do" linked to users.

Backend is built on FastAPI framework and running on Uvicorn ASGI web server. Data Base is SQLite located in the backend folder. The first time launched, the application creates tables and fills them with data (Test user and test user's Todos).

There is a fake smtp server (MailHog) to intercept and view sent mails.

FrontEnd is built with ReactJS fonctional components and react hooks. Styles and components are BootStrap ReactJS components.

Servers are running inside docker containers. Docker-compose is used to manage them.

Docker volumes are binded with developer workstations for direct code modifications. Hot reload are supported for todo-api (FastAPI) and todo-frontend (ReactJS) containers.

Stack:
- FastAPI
- ReactJS, Bootstrap
- Celery, Redis, Flower
- PostgreSQL
- PGAdmin
- MailHog
- Nginx
- Docker and Docker-Compose

## Getting started

1. Create a copy .env.exemple and rename it to .env. Configure .env if needed. .env is file with environment variables used for project configuration.
2. Create all application containers running the file "start-docker-linux.sh"

Once launched, there will be available hosts:
- http://localhost:8081/ - FrontEnd application
- http://localhost:8083/docs - BackEnd Swagger documentions
- http://localhost:8081/flower/ - Flower to view Celery Tasks
- http://localhost:8085/ - MailHog to view mails sent by application
- http://localhost:8086/ - PGAdmin to veiw DB tables and data

## Some useful commands

Build (or rebuild) the containers and launch all services:
```
docker-compose up --build --force-recreate
```

Stop all services:

```
docker-compose down
```
Launch a new instance of the docker-compose service using docker-compose (starting a new container and running /bin/sh inside). This is useful for container debugging:
```
docker-compose run todo-api /bin/sh
```
Execute a command inside a running container for service todo-my-service (here are a running a /bin/sh inside todo-api container):
```
docker-compose exec todo-api /bin/sh
```
Read a file from a container (to list all docker containers run docker ps -a):
```
docker container cp dadd0a5984de5c7f1dac6300a284decf3cad897180c370b8ecab647d3202fd43:/app/package.json -
```
Run tests inside todo-api container:
```
docker-compose exec todo-api python -m pytest tests/
```
Run mypy inside todo-api container:
```
docker-compose run todo-api mypy /code/app
```
Run shell inside FastAPI container:
```
docker-compose exec todo-api /bin/sh
```
Restart docker container in command line (in this exemple worker is todo-api):
```
docker-compose restart todo-api
```