# from .local_storage import LocalStorage
# from .s3_storage import S3Storage
from core.adapters.storage import aws_s3_adapter

class StorageFactory:
    @staticmethod
    def get_storage_adapter(storage_type):
        if storage_type == "local":
            pass # Implement local storage adapter creation logic here
        elif storage_type == "s3":
            
            return aws_s3_adapter()
        else:
            raise ValueError(f"Unknown storage type: {storage_type}")
