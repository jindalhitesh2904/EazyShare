from django.urls import path
from . import views
from .views import home

urlpatterns = [
	path('', views.home,name = 'Home'),
    path('about',views.about,name='About'),
    path('contact',views.contact,name='Contact'),
    path('sign_up',views.sign_up,name='SignUp'),
    path('login',views.signin,name='Login'),
    path('logout',views.logoutUser,name='Logout'),
]