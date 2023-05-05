import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

azure_storage_account_key = 'dsfghjkl;ertyuiop3497yt90vwye9ptmuva4nu8tbp9w435m[ty0a3w'

try:
    blob_service_client = BlobServiceClient.from_connection_string( azure_storage_account_key )

    # Quickstart code goes here

except Exception as ex:
    print('Exception:')
    print(ex)
