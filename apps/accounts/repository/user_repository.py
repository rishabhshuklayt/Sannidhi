from apps.accounts.models import User

class UserRepository:

    def get_by_email(self, email):
        return User.objects.filter(
            email=email
        ).first()
    
    def create_user(self, username: str, email: str, password: str):
         return User.objects.create(
            email=email,
            password=password,
            username=username
        )
