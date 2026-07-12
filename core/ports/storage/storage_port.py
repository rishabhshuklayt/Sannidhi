from abc import ABC, abstractmethod

class StoragePort(ABC):
    @abstractmethod
    def save_file(self, file_path: str, data: bytes):
        pass

    @abstractmethod
    def read_file(self, file_path: str) -> bytes:
        pass

    @abstractmethod
    def delete_file(self, file_path: str):
        pass