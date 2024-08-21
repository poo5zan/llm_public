from enum import Enum

class StorageProvider(Enum):
    FILE_STORAGE = 1
    MIN_IO_STORAGE = 2
    S3_STORAGE = 3