from django.shortcuts import render
from rest_framework import viewsets
from train.models import Train, Station, Booking, Review
from train.serializers import TrainSerializer, StationSerializer, BookingSerializer, ReviewSerializer
from rest_framework import filters, pagination

# Create your views here.
class TrainPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = page_size
    max_page_size = 100

class TrainViewSet(viewsets.ModelViewSet):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer
    filter_backends = [filters.SearchFilter]
    pagination_class = TrainPagination
    search_fields = ['station__name', 'train_name']

class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
