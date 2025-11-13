from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_type', 'country', 'skill_level', 'created_at']
    list_filter = ['user_type', 'skill_level', 'country']
    search_fields = ['user__username', 'user__email', 'country']
    readonly_fields = ['created_at']
