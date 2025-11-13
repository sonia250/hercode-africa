from django.db import models
from django.contrib.auth.models import User

class Tutorial(models.Model):
    """Programming tutorials and resources"""
    DIFFICULTY_CHOICES = (
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    )
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='beginner')
    category = models.CharField(max_length=100)
    duration = models.IntegerField(help_text="Estimated duration in minutes")
    video_url = models.URLField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']


class Progress(models.Model):
    """Track user progress on tutorials"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress')
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE, related_name='user_progress')
    completed = models.BooleanField(default=False)
    completion_date = models.DateTimeField(null=True, blank=True)
    time_spent = models.IntegerField(default=0, help_text="Time spent in minutes")
    notes = models.TextField(blank=True)
    
    def __str__(self):
        status = "Completed" if self.completed else "In Progress"
        return f"{self.user.username} - {self.tutorial.title} ({status})"
    
    class Meta:
        unique_together = ['user', 'tutorial']
        ordering = ['-completion_date']
        verbose_name_plural = "Progress records"


class Rating(models.Model):
    """User ratings for tutorials"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE, related_name='ratings')
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1-5 stars
    review = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} rated {self.tutorial.title}: {self.rating}/5"
    
    class Meta:
        unique_together = ['user', 'tutorial']
        ordering = ['-created_at']
