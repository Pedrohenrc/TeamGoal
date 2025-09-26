from django.db import models
from users.models import CustomUser
# Create your models here.

class Contribution(models.Model):
    title = models.CharField(max_lenght=100)
    created_at = models.DateTimeField(auto_now_add=True)
    goal = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="contributions")
    progresso = models.FloatField(default=0)