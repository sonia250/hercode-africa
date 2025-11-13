from django.contrib import admin
from .models import Tutorial, Progress, Rating

@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'difficulty', 'duration', 'created_by', 'created_at']
    list_filter = ['difficulty', 'category', 'created_at']
    search_fields = ['title', 'description', 'category']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'tutorial', 'completed', 'time_spent', 'completion_date']
    list_filter = ['completed', 'completion_date']
    search_fields = ['user__username', 'tutorial__title']

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['user', 'tutorial', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['user__username', 'tutorial__title']
    readonly_fields = ['created_at']
