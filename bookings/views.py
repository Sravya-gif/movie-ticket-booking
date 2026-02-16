from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import Seat, Booking
from movies.models import Show


# 🔹 Show seat layout
def seat_selection(request, show_id):
    show = get_object_or_404(Show, id=show_id)

    seats = Seat.objects.filter(show=show)

    # ✅ Proper seat sorting (A1, A2, ..., A10)
    seats = sorted(
        seats,
        key=lambda s: (s.seat_number[0], int(s.seat_number[1:]))
    )

    context = {
        "show": show,
        "seats": seats
    }

    return render(request, "seat_selection.html", context)


# 🔹 Confirm booking
@login_required
@transaction.atomic
def book_seat(request):
    if request.method == "POST":

        seat_ids = request.POST.get("selected_seats")
        show_id = request.POST.get("show_id")

        if not seat_ids:
            return redirect("movie_list")

        show = get_object_or_404(Show, id=show_id)

        seat_list = seat_ids.split(",")

        # 🔒 Lock selected seats to prevent race condition
        seats = Seat.objects.select_for_update().filter(
            id__in=seat_list,
            show=show
        )

        # ❌ If any seat already booked → stop
        for seat in seats:
            if seat.is_booked:
                return redirect("movie_list")

        # ✅ Create booking
        booking = Booking.objects.create(
            user=request.user,
            show=show
        )

        # ✅ Mark seats booked
        for seat in seats:
            seat.is_booked = True
            seat.save()
            booking.seats.add(seat)

        # ✅ SHOW CONFIRMATION PAGE
        return render(request, "booking_confirmation.html", {
            "booking": booking
        })

    # If someone accesses URL directly
    return redirect("movie_list")
