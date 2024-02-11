from rest_framework import serializers
from account.serializers import UserSerializer
from account.models import UserAccount
from .models import Train, Station, Booking, Review, Seat

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ['id', 'seat_no', 'is_booked']

class TrainSerializer(serializers.ModelSerializer):
    all_seats = SeatSerializer(many=True)

    class Meta:
        model = Train
        fields = '__all__'

    def update(self, instance, validated_data):
        seats_data = validated_data.pop('all_seats', None)
        if seats_data is not None:
            instance.all_seats.clear()
            for seat_data in seats_data:
                seat = Seat.objects.create(**seat_data)
                instance.all_seats.add(seat)
        return super().update(instance, validated_data)

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
