from django.db import models
from django.contrib.auth.models import (AbstractUser, BaseUserManager, PermissionsMixin)


# Create your models here.

class User(AbstractUser):
    pass
    # designation = models.CharField(max_length=100, blank=True, null=True)
    
