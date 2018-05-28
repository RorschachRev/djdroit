from django.contrib import admin
from .models import Store, Booth, Exhibitor
from login.models import Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Store)
admin.site.register(Booth)
admin.site.register(Exhibitor)

