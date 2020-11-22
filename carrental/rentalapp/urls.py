from django.urls import path
from . import views
from .views import home,about,contact,sign_up,signin,logoutUser,book_vehicle,add_vehicle

urlpatterns = [
	path('', views.home,name = 'Home'),
    path('about',views.about,name='About'),
    path('contact',views.contact,name='Contact'),
    path('sign_up',views.sign_up,name='SignUp'),
    path('login',views.signin,name='Login'),
    path('logout',views.logoutUser,name='Logout'),
    path('book_vehicle',views.book_vehicle,name='book_vehicle'),
    path('add_vehicle',views.add_vehicle,name='add_vehicle'),
]