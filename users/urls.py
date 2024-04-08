from django.contrib.auth import get_user_model
from rest_framework.routers import DefaultRouter
from django.urls import path


from . import views

router = DefaultRouter()
router.register("users", views.UserViewSet)

User = get_user_model()


urlpatterns = [
    path(
        'users/', views.UserViewSet.as_view({'post': 'create', 'get': 'list'}), name='user-list'),
    path('users/me/',
         views.UserViewSet.as_view({'get': 'me'}), name='user-me'),
    path('users/referral/',
         views.UserViewSet.as_view({'get': 'referral'}), name='user-referral')
]
