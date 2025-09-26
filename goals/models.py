from django.db import models
from teams.models import Team
from users.models import CustomUser
# Create your models here.

class Goal(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendente'),
        ('in_progress', 'Em Progresso'),
        ('completed', 'Concluída'),
    ]

    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="goals")
    title = models.CharField(max_length=150)
    description = models.TextField()
    deadline = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.team.name})"