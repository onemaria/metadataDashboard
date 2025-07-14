### Intro

This project uses [Uvicorn as a web server](https://www.uvicorn.org/) and [FastAPI web framework](https://fastapi.tiangolo.com/) to make fetch metadata
from [CrossRef](https://api.crossref.org/swagger-ui/index.html), cache it in a Redis DB and store it in a Postgres DB.

This microservice connects to a locally running Keycloak, Postgres and Redis database.

![fastAPI - metadataDashboard.png](fastAPI%20-%20metadataDashboard.png)
![keycloak - metadataDashboard.png](keycloak%20-%20metadataDashboard.png)
![authentication - metadataDashboard.png](authentication%20-%20metadataDashboard.png)

### Requirements
To run the project you need Python 3.12, Docker, docker-compose and pipenv.
Run the following commands:

```commandline
pipenv install
```

Run the below command o see which environment you are using, then select that virtual env (perhaps from IDE interface)
`pipenv --venv`

### Run the web server

Run the web server and build the docker compose for Keycloak, Redis and Postgres from docker-compose.yaml.

`uvicorn main:app --reload`
```commandline
docker-compose up --build
```

You can also run all 4: FastAPI app, Keycloak, Redis and Postgres from the docker-compose.yaml file but you will need to
modify the URL of the clients.
```commandline
docker-compose up --build
```

### Keycloak

Keycloak runs using the existing docker-compose.yaml. To check that it runs properly you can try the below cURL command

```
curl -X POST "http://localhost:8080/realms/testrealm/protocol/openid-connect/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "client_id=my-client" \
  -d "client_secret=omBL1mGAuXhocxdAs7rQDGJPHOZ37qmV" \
  -d "username=testuser" \
  -d "password=testpassword" \
  -d "grant_type=password"
```

The Keycloak login is:
```commandline
username: testuser
password: testpassword
```
However, the login is not necessary to access the DBs, it can be made a dependency but for now the login is only needed
to retrieve an access token.

### Postgres
Here you can see the metadata of all Journals or query Journals by ID. There are 2 endpoints:
1. postgres/journals
2. postgres/journals/{journal_id}

### Redis
The DB caches responses for the Health Journal category for 24h and if the same CrossRef fetch command is run, 
it will return the response from the cache. This can be of course extended for any or all categories of data.
There are 3 endpoints:
1. redis
2. redis/{key}
3. redis/{key}

### Metadata
This application is fetching Health Journal metadata from CrossRef and saves it in PostgresDB.

The endpoint used is:
1. metadata/fetch_crossref_journals

