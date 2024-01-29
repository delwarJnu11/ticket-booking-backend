from django.urls import path,include
from rest_framework.routers import DefaultRouter
from train.views import TrainViewSet,SeatListAPIView, StationViewSet, BookingViewSet, ReviewViewSet


router = DefaultRouter()

router.register('trains', TrainViewSet)
router.register('stations', StationViewSet)
router.register('bookings', BookingViewSet)
router.register('reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('seats/', SeatListAPIView.as_view(), name='seats'),
]