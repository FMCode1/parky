from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Booking
from .forms import BookingForm

@login_required
def booking_list(request):
    bookings = Booking.objects.filter(renter=request.user)
    return render(request, 'bookings/bookings.html', {'bookings': bookings})

@login_required
def booking_create(request):
    form = BookingForm(request.POST or None)
    if form.is_valid():
        booking = form.save(commit=False)
        booking.renter = request.user
        booking.save()
        return redirect('bookings:list')
    return render(request, 'bookings/booking_form.html', {'form': form})

@login_required
def booking_update(request, pk):
    booking = get_object_or_404(Booking, pk=pk, renter=request.user)
    form = BookingForm(request.POST or None, instance=booking)
    if form.is_valid():
        form.save()
        return redirect('bookings:list')
    return render(request, 'bookings/booking_form.html', {'form': form})

@login_required
def booking_delete(request, pk):
    booking = get_object_or_404(Booking, pk=pk, renter=request.user)
    if request.method == 'POST':
        booking.delete()
        return redirect('bookings:list')
    return render(request, 'bookings/booking_confirm_delete.html', {'booking': booking})