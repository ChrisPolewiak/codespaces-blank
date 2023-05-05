import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

connect_str = os.getenv('dsfghjkl;ertyuiop3497yt90vwye9ptmuva4nu8tbp9w435m[ty0a3w')

try:
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    # Quickstart code goes here

except Exception as ex:
    print('Exception:')
    print(ex)
