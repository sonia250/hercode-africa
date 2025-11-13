from django.contrib import admin
from .models import MentorshipRequest, PeerGroup, MentorshipSession

@admin.register(MentorshipRequest)
class MentorshipRequestAdmin(admin.ModelAdmin):
    list_display = ['mentee', 'mentor', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['mentee__username', 'mentor__username']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(PeerGroup)
class PeerGroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'focus_area', 'member_count', 'created_by', 'created_at']
    list_filter = ['focus_area', 'created_at']
    search_fields = ['name', 'focus_area', 'description']
    filter_horizontal = ['members']
    readonly_fields = ['created_at']

@admin.register(MentorshipSession)
class MentorshipSessionAdmin(admin.ModelAdmin):
    list_display = ['mentor', 'mentee', 'topic', 'scheduled_time', 'status']
    list_filter = ['status', 'scheduled_time']
    search_fields = ['mentor__username', 'mentee__username', 'topic']
    readonly_fields = ['created_at']
