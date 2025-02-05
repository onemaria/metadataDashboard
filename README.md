### Intro

This project uses [Uvicorn](https://www.uvicorn.org/) and [FasAPI](https://fastapi.tiangolo.com/).

The application is a simple Redis Microservice running using Uvicorn as a web server and FastAPI web framework.
The microservice connects to a locally runing Redis database and supports CRUD operations.

Redis is an open source (BSD licensed), in-memory data structure store, used as a database.

Uvicorn is an ASGI web server implementation for Python.

### Requirements
To run the project you need Python 3.12 and Docker.
Run the following commands:

`pip install pipenv`

`pipenv shell`

`pipenv install`

`pipenv --venv` - to see which environment you are using, then select that virtual env (perhaps from IDE interface)

### Run the server

`uvicorn main:app --reload`

The server communicates with a local Redis running in a docker container. To pull the redis docker image and then start the container do:

`docker pull redis`

`docker run -p 6379:6379 -v redis-data:/data redis`

### Generate python client

To generate a client you must generate an openapi schema of the service. Based on this schema
openapi-generator will generate a python client.

You will need Java (it was tested with Java 11) to run the openapi-generator-cli.jar as well as the _build_ python package.
```commandline
sudo apt update
sudo apt install openjdk-11-jdk
pip install --upgrade setuptools
bash scripts/generate-client.sh
```

### Access the redis CLI 
Install redis-cli:

`sudo apt update`

`sudo apt install redis-tools`

Access redis-cli

`redis-cli`

Here you can set, get or delete key value pairs:
- set `set KEY VALUE`
- get `get KEY`
- delete `delete KEY`


# keycloak setup

Keycloak can be run using the existing docker-compose.

Test Keycloak is running correctly:

```
curl -X POST "http://localhost:8080/realms/testrealm/protocol/openid-connect/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "client_id=my-client" \
  -d "client_secret=omBL1mGAuXhocxdAs7rQDGJPHOZ37qmV" \
  -d "username=testuser" \
  -d "password=testpassword" \
  -d "grant_type=password"
```
