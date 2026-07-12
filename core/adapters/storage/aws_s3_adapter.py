
from core.ports.storage.storage_port import StoragePort

class AWSS3Adapter(StoragePort):
    def __init__(self, s3_client, bucket_name):
        self.s3_client = s3_client
        self.bucket_name = bucket_name

    def save_file(self, file_path: str, data: bytes):
        self.s3_client.put_object(Bucket=self.bucket_name, Key=file_path, Body=data)

    def read_file(self, file_path: str) -> bytes:
        response = self.s3_client.get_object(Bucket=self.bucket_name, Key=file_path)
        return response['Body'].read()

    def delete_file(self, file_path: str):
        self.s3_client.delete_object(Bucket=self.bucket_name, Key=file_path)