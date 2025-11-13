from django.db import models
from django.contrib.auth.models import User

class MentorshipRequest(models.Model):
    """Mentee requests for mentorship"""
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    )
    
    mentee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentorship_requests')
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentor_requests')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.mentee.username} → {self.mentor.username} ({self.status})"
    
    class Meta:
        ordering = ['-created_at']


class PeerGroup(models.Model):
    """Peer learning groups"""
    name = models.CharField(max_length=200)
    description = models.TextField()
    focus_area = models.CharField(max_length=100)
    max_members = models.IntegerField(default=20)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_groups')
    members = models.ManyToManyField(User, related_name='peer_groups', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    def member_count(self):
        return self.members.count()
    
    class Meta:
        ordering = ['-created_at']


class MentorshipSession(models.Model):
    """Scheduled mentorship sessions"""
    STATUS_CHOICES = (
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )
    
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentor_sessions')
    mentee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentee_sessions')
    topic = models.CharField(max_length=200)
    scheduled_time = models.DateTimeField()
    duration = models.IntegerField(help_text="Duration in minutes")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    notes = models.TextField(blank=True)
    feedback = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.mentor.username} ↔ {self.mentee.username} - {self.topic}"
    
    class Meta:
        ordering = ['-scheduled_time']
