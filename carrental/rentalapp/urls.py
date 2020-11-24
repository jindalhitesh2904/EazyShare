from django.urls import path
from . import views
from .views import home,about,contact,sign_up,signin,logoutUser,book_vehicle,add_vehicle,ListMyVehicles,EditProfile,CreateBooking,BookBooking,MyBorrowings,EndBooking
from .views import ViewProfile
urlpatterns = [
	path('', views.home,name = 'Home'),
    path('about',views.about,name='About'),
    path('contact',views.contact,name='Contact'),
    path('sign_up',views.sign_up,name='SignUp'),
    path('login',views.signin,name='Login'),
    path('logout',views.logoutUser,name='Logout'),
    path('book_vehicle',views.book_vehicle,name='book_vehicle'),
    path('add_vehicle',views.add_vehicle,name='add_vehicle'),
    path('list_my_vehicles',ListMyVehicles.as_view(),name='list_my_vehicles'),
    path('edit_profile',EditProfile.as_view(),name='edit_profile'),
    path('create_booking/<slug:vehicle_id>/',CreateBooking,name='create_booking'),
    path('book_booking/<slug:booking_id>/',BookBooking,name='book_booking'),
    path('my_borrowings',MyBorrowings,name='my_borrowings'),
    path('end_booking/<slug:borrowing_id>/',EndBooking,name='end_booking'),
    path('view_profile/<slug:username>/',ViewProfile,name='view_profile'),
]