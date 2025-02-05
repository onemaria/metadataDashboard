from keycloak import KeycloakOpenID
from clients.config import settings


# Initialize Keycloak client with default settings
def initialize_keycloak_client():
    keycloak_client = KeycloakOpenID(
        server_url=settings.server_url,
        client_id=settings.client_id,
        realm_name=settings.realm,
        client_secret_key=settings.client_secret,
        verify=False
    )
    return keycloak_client


