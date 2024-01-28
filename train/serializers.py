from rest_framework import serializers
from .models import Train, Station, Booking, Review

class TrainSerializer(serializers.ModelSerializer):
    station = serializers.StringRelatedField(many=False)
    class Meta:
        model = Train
        fields = '__all__'

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