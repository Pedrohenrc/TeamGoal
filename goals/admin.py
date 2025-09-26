from django.contrib import admin
from .models import Goal
# Register your models here.

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('team', 'status', 'deadline', 'created_at') 
    search_fields = ('status', 'description')        
    list_filter = ('team', 'title')