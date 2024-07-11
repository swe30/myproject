from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    primary_email = models.EmailField()
    emails = models.ManyToManyField('Email')

    def __str__(self):
        return self.user.username

class Email(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
    
class UploadedFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    comments = models.ManyToManyField('Comment')

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()    


class UserProfile(models.Model):
    ...
    @property
    def location_flag(self):
        # Return the flag URL based on location
        return f"https://example.com/flags/{self.location}.png"


class UserProfile(models.Model):
    ...
    @property
    def location_flag(self):
        # Return the flag URL based on location
        return f"https://example.com/flags/{self.location}.png"

    