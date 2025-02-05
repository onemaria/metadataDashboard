from models import authConfiguration


settings = authConfiguration(
    server_url="http://localhost:8080/",
    realm="testrealm",
    client_id="my-client",
    client_secret="omBL1mGAuXhocxdAs7rQDGJPHOZ37qmV",
    authorization_url="http://localhost:8080/realms/testrealm/protocol/openid-connect/auth",
    token_url="http://localhost:8080/realms/testrealm/protocol/openid-connect/token",
)
