from django.db import models
from account.models import UserAccount
from .constants import TIME_CHOICES,SEAT_CHOICES

# Create your models here.
class Station(models.Model):
    name = models.CharField(max_length = 50)
    slug = models.SlugField(max_length = 55, unique = True)

    def __str__(self) -> str:
        return f'{self.name}'

class Train(models.Model):
    train_name = models.CharField(max_length=50, unique=True)
    train_id = models.CharField(max_length=20, unique=True)
    departure_time = models.CharField(max_length=20, choices=TIME_CHOICES)
    seats_available = models.PositiveIntegerField()
    start_station = models.CharField(max_length=50, null=True, blank=True)
    end_station = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    all_seats = models.ManyToManyField('Seat', related_name='trains', blank=True)

    def __str__(self) -> str:
        return f'{self.train_name}-{self.train_id}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.all_seats.exists():
            self.all_seats.clear()
            all_seats = Seat.objects.all()

            for i, seat in enumerate(self.all_seats.all()):
                seat.is_booked = False
                seat.save()

            self.all_seats.add(*all_seats)

class Seat(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE, null=True, blank=True)
    seat_number = models.CharField(max_length=3, choices=SEAT_CHOICES, default='A1')
    is_booked = models.BooleanField(default=False)

    class Meta:
        ordering = ['seat_number']

    def __str__(self) -> str:
        return self.seat_number

class Booking(models.Model):
    passenger = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    seat_number = models.PositiveIntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)
    journey_date = models.DateField(null = True, blank = True)

    def __str__(self) -> str:
        return f'{self.passenger.first_name} booking ticket for {self.train.train_name}'

class Review(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    train = models.ForeignKey(Train, on_delete = models.CASCADE, related_name='review')

    def __str__(self) -> str:
        return f'{self.name} review for {self.train.train_name}'

