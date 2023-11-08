import os
import yaml
import chromadb
from chromadb.utils import embedding_functions

from .auth import retrieve_secret
from .data_utils import initialize_documents

# initialize config
base_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(base_dir, 'config.yaml')
with open(config_path, 'r') as config_file:
    config = yaml.safe_load(config_file)

app_settings = config['AppSettings']
if app_settings['UseAzureKeyVault']:
    az_settings = config['AzureKeyVaultSettings']
    api_key = retrieve_secret(az_settings['key_vault_name'], az_settings['openai_key_name'])
    api_base = retrieve_secret(az_settings['key_vault_name'], az_settings['openai_endpoint_name'])
else:
    env_settings = config['EnvironmentVariableSettings']
    api_key = os.getenv(env_settings['openai_key'])
    api_base = os.getenv(env_settings['openai_endpoint'])

chroma_settings = config['ChromaSettings']
persist_directory = chroma_settings['persist_directory']
documents_directory = chroma_settings['documents_directory']
collection_name = chroma_settings['collection_name']

# initialize chroma client and collection for testing
chroma_client = chromadb.PersistentClient(path=persist_directory)
chroma_collection = chroma_client.get_or_create_collection(name=collection_name)
data_utils.initialize_documents(documents_directory, chroma_collection)