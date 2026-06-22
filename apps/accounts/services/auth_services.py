from apps.accounts.models import User
from apps.accounts.repository.user_repository import UserRepository
class AuthService():
    def __init__(self,  user_repository,email_port):
        self.user_repository = user_repository
        self.email_port = email_port


    def register_user(self, username: str, email: str, password: str):
    #    check if user already exists
        existing_user = self.user_repository.get_by_email(self,email=email)
        if existing_user:
            raise Exception("User already exists")
        new_user = self.user_repository.create_user(self, username=username, email=email, password=password)
        if not new_user:
            raise Exception("User registration failed")
        self.email_port.get_email_adapter().send_email(
            subject="Welcome to our platform",
            message="Thank you for registering with us.",
            from_email="",
            recipient_list=[email]
        )
        return new_user