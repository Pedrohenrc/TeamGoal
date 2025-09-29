from django.db import models
from users.models import CustomUser
from goals.models import Goal
# Create your models here.
class SubGoal(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name="subtasks")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    assigned_to = models.ForeignKey(
        CustomUser, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="subtasks"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def fechar_subtask(self):
        self.is_completed = True
        self.save()
        if hasattr(self.goal, "update_progress"):
            self.goal.update_progress()

    def __str__(self):
        return f"{self.title} ({'Done' if self.is_completed else 'Pending'})"
    