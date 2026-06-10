from django.contrib import admin
from django.urls import path, include
from movies.views import location_list

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', location_list, name='home'),

    path('movies/', include('movies.urls')),
    
    path('', include('bookings.urls')),
]
