from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegistrationForm(UserCreationForm):
    """Extended user registration form"""
    email = forms.EmailField(required=True)
    user_type = forms.ChoiceField(
        choices=Profile.USER_TYPES,
        required=True,
        widget=forms.RadioSelect
    )
    country = forms.CharField(max_length=100, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
            # Create profile
            Profile.objects.create(
                user=user,
                user_type=self.cleaned_data['user_type'],
                country=self.cleaned_data['country']
            )
        return user


class ProfileUpdateForm(forms.ModelForm):
    """Form for updating user profile"""
    class Meta:
        model = Profile
        fields = ['profile_picture', 'country', 'bio', 'skill_level', 
                  'areas_of_interest', 'expertise', 'years_experience', 'availability']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
            'areas_of_interest': forms.Textarea(attrs={'rows': 3, 'placeholder': 'e.g., Python, Web Development, Data Science'}),
            'expertise': forms.Textarea(attrs={'rows': 3, 'placeholder': 'e.g., Django, React, Machine Learning'}),
        }