from django.db import models
from django.contrib.auth.models import User
from movies.models import Show

class Seat(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.show} - Seat {self.seat_number}"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    seats = models.ManyToManyField(Seat)
    booking_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.user.username} for {self.show}"
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Seat
from movies.models import Show


@receiver(post_save, sender=Show)
def create_seats_for_show(sender, instance, created, **kwargs):
    if created:
        rows = "ABCDEFGH"
        for row in rows:
            for num in range(1, 11):
                Seat.objects.create(
                    show=instance,
                    seat_number=f"{row}{num}"
                )
