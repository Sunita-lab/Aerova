

from django.db import models

# Create your models here.
class Flight(models.Model):
    flight_number = models.CharField(max_length = 10)
    origin = models.CharField(max_length = 100)
    destination = models.CharField(max_length = 100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    
    def __str__(self):
        return f"{self.flight_number}: {self.origin} to {self.destination}"
