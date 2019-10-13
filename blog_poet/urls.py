from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('inventors.urls')),
    path('registration/',include('registration.urls')),

]
