import os
import functions_framework

from google.cloud import storage
storage_client = storage.Client()

@functions_framework.http
def get_blob(request):
    bucket = storage_client.bucket(os.environ.get('BUCKET'))
    blob = bucket.blob(os.environ.get('FILE'))
    resume = blob.download_as_text()
    headers = {'Content-Type': 'application/json'}
    return (resume, 200, headers)