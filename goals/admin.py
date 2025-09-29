from django.contrib import admin
from .models import Goal
from subgoals.models import SubGoal
# Register your models here.

class SubGoalInline(admin.TabularInline):  # ou StackedInline se preferir em blocos
    model = SubGoal
    extra = 1  # mostra 1 linha vazia para adicionar subtarefas
    autocomplete_fields = ("assigned_to",)
    fields = ("title", "is_completed", "assigned_to", "created_at")
    readonly_fields = ("created_at",)

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('title', 'team', 'status', 'deadline','progress', 'created_at', 'updated_at') 
    search_fields = ('title', 'description', 'team__name')        
    list_filter = ('status', 'title')