from django.db import models
from account.models import UserAccount

# Create your models here.
class Station(models.Model):
    name = models.CharField(max_length = 50)
    slug = models.SlugField(max_length = 55, unique = True)

    def __str__(self) -> str:
        return f'{self.name}'


class Train(models.Model):
    train_name = models.CharField(max_length = 50)
    train_id = models.CharField(max_length = 20)
    schedule = models.DateTimeField()
    seats_available = models.PositiveIntegerField()
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='station', default=None, null=True)


    def __str__(self) -> str:
        return f'{self.train_name}-{self.train_id}'

class Booking(models.Model):
    passenger = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    seat_number = models.PositiveIntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)

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

