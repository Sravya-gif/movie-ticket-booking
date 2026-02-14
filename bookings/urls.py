from django.urls import path
from . import views

urlpatterns = [
    path('seats/<int:show_id>/', views.seat_selection, name='seat_selection'),
    path('book-seat/', views.book_seat, name='book_seat'),
]
