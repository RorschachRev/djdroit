from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm, UserForm
from .models import Profile

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return HttpResponseRedirect('profile.html')
	else:
		form = UserCreationForm()
		return render(request, 'pages/signup.html', { 'form': form })

def expo(request):
	expo=""
	expomap=''
	return render(request,'pages/expo.html', { 'expo':expo, 'map':expomap  } )
	
def index(request):
	return render(request,'pages/index.html', { 'index':index } )
	
def shop(request):
	return render(request,'pages/shop.html', { 'shop':shop } )

def members(request):
	return render(request,'pages/members.html', { 'members':members } )

def ardemo(request):
	return render(request,'pages/ardemo.html', { 'ardemo':ardemo } )

def contact(request):
	return render(request,'pages/contact.html', { 'contact':contact } )
	
def expomap(request):
	return render(request,'pages/expomap.html', { 'map':expomap } )
	
def edit(request):
	return render(request,'pages/edit.html', { 'edit':edit } )

#@login_required
#@transaction.atomic
def update_profile(request):
    profile_info = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=profile_info)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return HttpResponseRedirect('profile.html')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile_info)
    return render(request, 'pages/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
