from apps.accounts.models import User

class UserRepository:

    def get_by_email(self, email):
        return User.objects.filter(
            email=email
        ).first()
    
    def create_user(self, username: str, email: str, password: str):
         return User.objects.create_user(
            email=email,
            password=password,
            username=username
        )
    
    def delete_user(self, email: str):
        user = self.get_by_email(email=email)
        if user:
            user.delete()
            return True
        return False
    
    def update_user(self, email: str, **kwargs):
        user = self.get_by_email(email=email)
        if user:
            for key, value in kwargs.items():
                setattr(user, key, value)
            user.save()
            return user
        return None
    
    def get_all_users(self):
        return User.objects.all()
    
    def deactivate_user(self, email: str):
        user = self.get_by_email(email=email)
        if user:
            user.is_active = False
            user.save()
            return user
        return None
