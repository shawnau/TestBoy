import os
import yaml
import chromadb
from chromadb import ClientAPI, Collection

from .auth import retrieve_secret
from .data_utils import initialize_documents

class Settings:
    initialized = False

    api_key: str = None
    api_base: str = None
    model: str = None

    persist_directory: str = None
    documents_directory: str = None
    collection_name: str = None

    chroma_client: ClientAPI = None
    chroma_collection: Collection = None


settings = Settings()

def config(config_path: str):
    """config testboy settings
    config_path (str): path to config file
    """
    with open(config_path, 'r') as config_file:
        config = yaml.safe_load(config_file)

    app_settings = config['AppSettings']
    settings.model = app_settings['Model']
    if app_settings['UseAzureKeyVault']:
        az_settings = config['AzureKeyVaultSettings']
        settings.api_key = retrieve_secret(az_settings['key_vault_name'], az_settings['openai_key_name'])
        settings.api_base = retrieve_secret(az_settings['key_vault_name'], az_settings['openai_endpoint_name'])
    else:
        env_settings = config['EnvironmentVariableSettings']
        settings.api_key = os.getenv(env_settings['openai_key'])
        settings.api_base = os.getenv(env_settings['openai_endpoint'])

    chroma_settings = config['ChromaSettings']
    settings.persist_directory = chroma_settings['persist_directory']
    settings.documents_directory = chroma_settings['documents_directory']
    settings.collection_name = chroma_settings['collection_name']

    # initialize chroma client and collection for testing
    settings.chroma_client = chromadb.PersistentClient(path=settings.persist_directory)
    settings.chroma_collection = settings.chroma_client.get_or_create_collection(name=settings.collection_name)
    data_utils.initialize_documents(settings.documents_directory, settings.chroma_collection)

    settings.initialized = True

