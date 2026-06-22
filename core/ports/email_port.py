from abc import ABC, abstractmethod

class EmailPort(ABC):
    @abstractmethod
    def send_email(self, subject: str, message: str, from_email: str, recipient_list: list):
        pass 