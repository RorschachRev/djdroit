"""mydj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from mydj import views

urlpatterns = [
    url(r'^$',  views.index, name='base'),
    url(r'^index.html$', views.index, name='index'),
    url(r'^login/$', auth_views.login, {'template_name': 'pages/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'pages/logout.html'}, name='logout'),
    url(r'^expo.html$', views.expo, name='expo'),
    url(r'^profile.html$', views.update_profile, name='profile'),
    url(r'^shop.html$', views.shop, name='shop'),
    url(r'^expomap.html$', views.expomap, name='expomap'),
    url(r'^edit.html$', views.edit, name='edit'),
    url(r'^admin/', admin.site.urls),
    url(r'^signup.html$', views.signup, name='signup'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

