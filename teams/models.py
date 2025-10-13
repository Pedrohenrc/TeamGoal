from django.db import models
from users.models import CustomUser
# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='owned_teams')
    members = models.ManyToManyField(CustomUser, related_name="teams", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
