from storage_service.storage_provider_base import StorageProviderBase

class S3StorageService(StorageProviderBase):
    def __init__(self, access_key: str, access_token: str) -> None:
        if access_key == "":
            raise ValueError("access_key is required")
        
        if access_token == "":
            raise ValueError("access_token is required")
        
        self.access_key = access_key
        self.access_token = access_token

    def save(self, run_id, data):
        pass