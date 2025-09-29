from django.contrib import admin
from .models import Goal
from subgoals.models import SubGoal
from users.models import CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    pass
class SubGoalInline(admin.TabularInline): 
    model = SubGoal
    extra = 1  
    autocomplete_fields = ("assigned_to",)
    fields = ("title", "is_completed", "assigned_to", "created_at")
    readonly_fields = ("created_at",)

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('title', 'team', 'status', 'deadline','progress', 'created_at', 'updated_at') 
    search_fields = ('title', 'description', 'team__name')        
    list_filter = ('status', 'team', 'deadline', 'created_at')
    ordering = ("-created_at",)
    inlines = [SubGoalInline]
    readonly_fields = ("created_at", "updated_at")
    autocomplete_fields = ("team",)