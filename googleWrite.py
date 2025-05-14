from io import BytesIO

from google.cloud import storage

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] must be set
storage_client = storage.Client()
blob = storage_client.bucket("my-bucket").blob("mydoc.pdf")
file_stream = BytesIO()
blob.download_to_file(file_stream)
reader = PdfReader(file_stream)