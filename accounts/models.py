from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """Extended user profile for HerCode Africa users"""
    USER_TYPES = (
        ('mentee', 'Mentee'),
        ('mentor', 'Mentor'),
        ('admin', 'Admin'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='mentee')
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    country = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Mentee specific fields
    skill_level = models.CharField(max_length=50, blank=True)
    areas_of_interest = models.TextField(blank=True, help_text="Comma-separated interests")
    
    # Mentor specific fields
    expertise = models.TextField(blank=True, help_text="Comma-separated expertise areas")
    years_experience = models.IntegerField(default=0, blank=True)
    availability = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.user_type}"
    
    class Meta:
        ordering = ['-created_at']
