from django.db import models
from account.models import UserAccount
from .constants import TIME_CHOICES,SEAT_CHOICES

# Create your models here.
class Station(models.Model):
    name = models.CharField(max_length = 50)
    slug = models.SlugField(max_length = 55, unique = True)

    def __str__(self) -> str:
        return f'{self.name}'
    
class Seat(models.Model):
    seat_no = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return self.seat_no

class Train(models.Model):
    train_name = models.CharField(max_length=50, unique=True)
    train_id = models.CharField(max_length=20, unique=True)
    departure_time = models.CharField(max_length=20, choices=TIME_CHOICES)
    seats_available = models.PositiveIntegerField()
    start_station = models.CharField(max_length=50)
    end_station = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    all_seats = models.ManyToManyField(Seat)

    def __str__(self):
        return self.train_name

class Booking(models.Model):
    user = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=14)
    nid = models.CharField(max_length=20)
    train = models.CharField(max_length=50)
    train_id = models.CharField(max_length=20)
    start_station = models.CharField(max_length=50)
    end_station = models.CharField(max_length=50)
    fare = models.DecimalField(max_digits=12, decimal_places=2)
    departure_time = models.CharField(max_length=20)
    seat_number = models.CharField(max_length=20)
    booking_date = models.DateTimeField(auto_now_add=True)
    journey_date = models.DateField(null = True, blank = True)

    def __str__(self) -> str:
        return f'{self.user} booking ticket for {self.train} Seat {self.seat_number}'

class Review(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    train = models.ForeignKey(Train, on_delete = models.CASCADE, related_name='review')

    def __str__(self) -> str:
        return f'{self.name} review for {self.train.train_name}'

