# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from account.views import UserRegistrationViewSet, UserLoginViewSet, UserLogoutViewSet, activate

router = DefaultRouter()
router.register('registration', UserRegistrationViewSet, basename='registration')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', UserLoginViewSet.as_view(), name='login'),
    path('logout/', UserLogoutViewSet.as_view(), name='logout'),
    path('activate/<str:uid64>/<str:token>/', activate, name='activate'),
]


