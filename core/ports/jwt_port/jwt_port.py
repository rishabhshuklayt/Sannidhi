
from abc import ABC , abstractmethod


class JWTPort(ABC):
    @abstractmethod
    def generate_token(self, user_id: int) -> str:
        pass
