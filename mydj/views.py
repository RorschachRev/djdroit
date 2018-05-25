from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UserForm#, ProfileForm
from mydj import settings
from .models import Subscription
#import stripe

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
    
# for STRIPE API testing    
def payment_form(request):
	#context = { "stripe_key": settings.STRIPE_PUBLIC_KEY }
	context = {}
	return render(request, "pages/payment_form.html", context)
	
# for STRIPE testing
def checkout(request):
	stripe.api_key = settings.STRIPE_SECRET_KEY
	# hardcoded for testing purposes
	new_sub = Subscription(
		price = 20,
		subscription = 1,
		web_shop_enabled = True,
	)
	
	if request.method == 'POST':
		token = request.POST.get('stripeToken')
	
	try:
		charge = stripe.Charge.create(
			amount = 2000, #amount is in pennies ¿?
			currency = 'usd',
			source = token,
			description = 'The subscription __str__()'
		)
		
		new_sub.charge_id = charge.id
	
	except stripe.error.CardError as ce:
		return False, ce
	
	else:
		new_sub.save()
		return redirect('pages/thank_you_page.html')
		
def thank_you(request):
	return render(request, 'pages/thank_you_page.html')
