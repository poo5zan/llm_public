
from storage_service.file_storage_service import FileStorageService
from storage_service.min_io_storage_service import MinIoStorageService
from storage_service.s3_storage_service import S3StorageService
from storage_service.storage_provider import StorageProvider

class StorageProviderFactory():
    def __init__(self, storage_provider: StorageProvider) -> None:
        self.storage_provider = storage_provider

    def get_storage_provider_instance(self):
        if self.storage_provider == StorageProvider.FILE_STORAGE:
            return FileStorageService()
        elif self.storage_provider == StorageProvider.MIN_IO_STORAGE:
            return MinIoStorageService()
        elif self.storage_provider == StorageProvider.S3_STORAGE:
            return S3StorageService()