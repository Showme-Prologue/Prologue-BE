from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True, max_length=50)
    profilePhoto = models.ImageField(blank=True, null=True, default='media/users/default.png', upload_to='users')
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} / {self.email}"
    