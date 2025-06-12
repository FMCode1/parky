from django.db import models
from django.conf import settings

class Booking(models.Model):
    renter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    spot = models.CharField(max_length=255)  # Replace with ForeignKey if needed
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed')])

    def __str__(self):
        return f'{self.renter.username} booked {self.spot} from {self.start_time} to {self.end_time}'