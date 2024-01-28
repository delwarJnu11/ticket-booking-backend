from django.urls import path, include
from rest_framework.routers import DefaultRouter
from account.views import UserListViewSet, UserRegistrationViewSet, UserLoginViewSet, UserLogoutViewSet, activate

router = DefaultRouter()
router.register('users', UserListViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('registration/', UserRegistrationViewSet.as_view(), name='registration'),
    path('login/', UserLoginViewSet.as_view(), name='login'),
    path('logout/', UserLogoutViewSet.as_view(), name='logout'),
    path('activate/<str:uid64>/<str:token>/', activate, name='activate'),
]


