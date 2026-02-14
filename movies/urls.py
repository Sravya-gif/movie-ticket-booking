from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('shows/<int:movie_id>/', views.show_list, name='show_list'),
]
