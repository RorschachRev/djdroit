from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from django.dispatch import receiver

class Profile(models.Model):
	is_exhibitor= models.BooleanField(default=False)
	#user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	company_name = models.TextField(max_length=200, blank=True)
	#is_artist = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()

class Booth(models.Model):
    booth_name= models.BooleanField(default=False)

class Store(models.Model):
    store_name= models.BooleanField(default=False)

class Exhibitor(models.Model):
    booth = models.ForeignKey(Booth)
    store =  models.ForeignKey(Store, related_name='shopping')
