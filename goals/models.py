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
    title = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    deadline = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.team.name})"

    @property
    def progress(self):
        total = self.subtasks.count()
        if total == 0:
            return 0
        completed = self.subtasks.filter(is_completed=True).count()
        return int((completed / total) * 100)
    
    
    def update_progress(self):
        if self.subtasks.exists() and self.subtasks.filter(is_completed=False).count() == 0:
            self.status = "completed"
            self.save()
    def fechar_meta(self):
        if self.subtasks.filter(is_completed=False).exists():
            return False
        self.status = "completed"
        self.save()
        return True


    