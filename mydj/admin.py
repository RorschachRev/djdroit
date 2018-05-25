from django.contrib import admin
from .models import Store, Booth, Exhibitor, Subscription#, Profile

# Register your models here.
#admin.site.register(Profile)
admin.site.register(Store)
admin.site.register(Booth)
admin.site.register(Exhibitor)
admin.site.register(Subscription)

