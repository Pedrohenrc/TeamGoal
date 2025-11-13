from django.contrib import admin
from .models import Contribution

@admin.register(Contribution)
class ContributionAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "goal", "subtask", "created_at")
    list_filter = ("goal", "user", "created_at")
    search_fields = ("user__username", "goal__title", "subtask__title")
    ordering = ("-created_at",)