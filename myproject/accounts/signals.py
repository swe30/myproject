from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_login_failed
from django.dispatch import receiver
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

@receiver(user_login_failed)
def login_failed(sender, credentials, request, **kwargs):
    user = User.objects.get(username=credentials['username'])
    user_profile = user.userprofile
    user_profile.failed_attempts += 1
    if user_profile.failed_attempts >= 3:
       user_profile.locked_until = timezone.now() + timedelta(minutes=5)
    user_profile.save()

@receiver(user_logged_in)
def login_success(sender, request, user, **kwargs):
    user_profile = user.userprofile
    user_profile.failed_attempts = 0
    user_profile.save()

