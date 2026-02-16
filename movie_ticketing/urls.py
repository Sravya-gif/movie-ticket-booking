from django.contrib import admin
from django.urls import path, include
from movies.views import location_list

urlpatterns = [
    path('admin/', admin.site.urls),

    # Homepage → Location selection page
    path('', location_list, name='home'),

    # Movies
    path('movies/', include('movies.urls')),

    # Booking
    path('', include('bookings.urls')),
]
