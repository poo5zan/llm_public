
from storage_service.storage_provider_base import StorageProviderBase


class FileStorageService(StorageProviderBase):
    def __init__(self, root_directory: str):
        if root_directory == "":
            raise Exception("root directory is required")

    def save(self, run_id, data):
        pass
    