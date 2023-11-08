from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

def retrieve_secret(key_vault_name: str, secret_name: str) -> str:
    kv_uri = f"https://{key_vault_name}.vault.azure.net"
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=kv_uri, credential=credential)
    return client.get_secret(secret_name).value