from django.contrib import admin
from .models import SubGoal

@admin.register(SubGoal)
class SubGoalAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "goal",
        "assigned_to",
        "is_completed",
        "created_at",
        "updated_at",
    )
    list_filter = ("is_completed", "goal", "assigned_to", "created_at")
    search_fields = ("title", "description", "goal__title", "assigned_to__username")
    ordering = ("-created_at",)
    autocomplete_fields = ("goal", "assigned_to")  # melhora desempenho se houver muitos registros
