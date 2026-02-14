from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

# Home view
def home(request):
    return render(request, "home.html")

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home page first
    path('', home, name='home'),

    # Movies page
    path('movies/', include('movies.urls')),

    # Booking routes
    path('', include('bookings.urls')),
]
