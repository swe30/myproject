from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Email

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    primary_email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'password', 'primary_email']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['location', 'emails']

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']