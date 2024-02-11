from django.urls import path,include
from rest_framework.routers import DefaultRouter
from train.views import TrainViewSet,SeatListAPIView, StationViewSet, BookingViewSet, ReviewViewSet


router = DefaultRouter()

router.register('trains', TrainViewSet,basename='trains')
router.register('stations', StationViewSet,basename='stations')
router.register('bookings', BookingViewSet,basename='bookings')
router.register('reviews', ReviewViewSet,basename='reviews')

urlpatterns = [
    path('', include(router.urls)),
    path('seats/', SeatListAPIView.as_view(), name='seats'),
]