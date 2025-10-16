# subgoals/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SubGoal
from contributions.models import Contribution

@receiver(post_save, sender=SubGoal)
def create_contribution_on_complete(sender, instance, created, **kwargs):
    if instance.is_completed:
        if not hasattr(instance, 'contribution'):
            user = instance.assigned_to
            if user:
                Contribution.objects.create(
                    subtask=instance,
                    goal=instance.goal,
                    user=user
                )
