
# from carrental.carrental.settings import MEDIA_URL
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('carrent/',include('rentalapp.urls')),
]+staticfiles_urlpatterns()
 
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)