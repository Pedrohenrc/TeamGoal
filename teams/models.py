from django.db import models
from users.models import CustomUser
import secrets
import uuid
# Create your models here.

class Team(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='owned_teams')
    members = models.ManyToManyField(CustomUser, related_name="teams", blank=True)
    code = models.CharField(max_length=10, unique=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = secrets.token_hex(4).upper() 
        super().save(*args, **kwargs)

class TeamJoinRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendente'),
        ('accepted', 'Aceito'),
        ('rejected', 'Rejeitado'),
    ]
    
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='join_requests')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='join_requests')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('team', 'user') 
    
    def __str__(self):
        return f"{self.user.username} → {self.team.name}"