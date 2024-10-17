from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, ProfileForm
from .models import Profile
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            # Save the user form and create the user instance
            user = user_form.save()

            # Create a profile instance, but don't save to database yet
            profile = profile_form.save(commit=False)
            profile.user = user  # Link profile to the user
            profile.save()  # Now save the profile instance

            messages.success(request, f'Account created for {user.username}!')
            return redirect('login')
    else:
        user_form = UserRegisterForm()
        profile_form = ProfileForm()

    return render(request, 'registration.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def profile(request):
    user_profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'profile.html', {'profile': user_profile})

def profiles(request, id):
    user_profile = get_object_or_404(Profile, user__id=id)
    return render(request, 'profile.html', {'profile': user_profile})

def edit_profile(request):
    user_profile = get_object_or_404(Profile, user=request.user)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=user_profile)
    
    return render(request, 'edit_profile.html', {'form': form, 'profile': user_profile})