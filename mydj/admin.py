from django.contrib import admin
from .models import Profile, Store, Booth, Exhibitor

# Register your models here.
admin.site.register(Profile)
admin.site.register(Store)
admin.site.register(Booth)
admin.site.register(Exhibitor)
