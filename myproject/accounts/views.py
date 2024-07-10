from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .views import UserRegistrationForm, UserProfileForm
from ipware import get_client_ip
from django_countries import countries
from .tasks import process_video


class RegisterView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            UserProfile.objects.create(user=user, primary_email=form.cleaned_data['primary_email'])
            return redirect('login')
        return render(request, 'accounts/register.html', {'form': form})
    

def get_user_location(request):
    ip, _ = get_client_ip(request)
    # Use a geolocation service to convert IP to location here
    return "Location based on IP"

class RegisterView(View):
    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            location = get_user_location(request)
            UserProfile.objects.create(user=user, primary_email=form.cleaned_data['primary_email'], location=location)
            return redirect('login')
        return render(request, 'accounts/register.html', {'form': form})    
    

class FileUploadView(View):
    def post(self, request):
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save(commit=False)
            uploaded_file.user = request.user
            uploaded_file.save()
            process_video.delay(uploaded_file.id)
            return redirect('file_list')
        return render(request, 'upload.html', {'form': form})    
