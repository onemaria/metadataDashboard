from models import authConfiguration


settings = authConfiguration(
    server_url="http://localhost:8080/",
    realm="realm",
    client_id="rns:realm:portal",
    client_secret="",
    authorization_url="http://localhost:8080/realms/realm/protocol/openid-connect/auth",
    token_url="http://localhost:8080/realms/realm/protocol/openid-connect/token",
)
