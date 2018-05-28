from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UserForm, ProfileForm

def signup(request):
	if request.method == 'POST':
		user_form = UserForm(request.POST)
		if user_form.is_valid():
			user_form.save()
		return HttpResponseRedirect('profile.html')
	else:
		user_form = UserForm()
		return render(request, 'pages/signup.html', { 'form': UserForm })

def expo(request):
	expo=""
	expomap=''
	return render(request,'pages/expo.html', { 'expo':expo, 'map':expomap  } )
	
def index(request):
	return render(request,'pages/index.html', { 'index':index } )
	
def shop(request):
	return render(request,'pages/shop.html', { 'shop':shop } )
	
def expomap(request):
	return render(request,'pages/expomap.html', { 'map':expomap } )
	
def edit(request):
	return render(request,'pages/edit.html', { 'edit':edit } )

#@login_required
#@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user)
    return render(request, 'pages/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })