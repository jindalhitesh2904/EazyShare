from django.urls import path
from . import views
from .views import home

urlpatterns = [
	path('', views.home,name = 'Home'),
    path('about',views.about,name='About'),
    path('contact',views.contact,name='Contact'),
]