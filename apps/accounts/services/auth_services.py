from apps.accounts.models import User
from apps.accounts.repository.user_repository import UserRepository
from apps.accounts.exceptions import UserAlreadyExistsException
from core.ports.jwt_port import jwt_port
class AuthService():
    def __init__(self,  user_repository,email_port, jwt_port):
        self.user_repository = user_repository
        self.email_port = email_port
        self.jwt_port = jwt_port


    def register_user(self, username: str, email: str, password: str):
    #    check if user already exists
        existing_user = self.user_repository.get_by_email(self,email=email)
        if existing_user:
            # raise userAlreadyExistsException("User already exists")
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
    
    def login_user(self, email: str, password: str):
        user = self.user_repository.get_by_email(self,email=email)
        if not user:
            raise Exception("User does not exist")
        if not user.check_password(password):
            raise Exception("Invalid password")
        tokens = self.jwt_port.generate_token(user_id=user)
        self.email_port.get_email_adapter().send_email(
            subject="Login Successful",
            message="You have successfully logged in.",
            from_email="",
            recipient_list=[email]
        )
        return tokens