from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to="profiles/", blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)

    def __str__ (self):
        return self.username