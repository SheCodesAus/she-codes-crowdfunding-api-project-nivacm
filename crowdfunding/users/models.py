from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    image = models.URLField(max_length=300)
    bio = models.CharField(max_length=500)

    def __str__(self):
        return self.username


