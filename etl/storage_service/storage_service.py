class StorageService():
    def __init__(self, storage_provider_instance) -> None:
        self.storage_provider_instance = storage_provider_instance

    def save(self, run_id, data):
        self.storage_provider_instance.save(run_id, data)