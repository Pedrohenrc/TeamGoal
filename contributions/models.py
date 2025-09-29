from django.db import models
from users.models import CustomUser
# Create your models here.

class Contribution(models.Model):
    subtask = models.ForeignKey("subgoals.SubGoal", on_delete=models.CASCADE, null=True, blank=True, related_name="contributions")
    goal = models.ForeignKey("goals.Goal", on_delete=models.CASCADE, null=True, blank=True, related_name="contributions")
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="contributions")
    progress = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.subtask and not self.goal:
            self.goal = self.subtask.goal
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user} - {self.subtask} ({self.progress}%)"