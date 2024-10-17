from django.urls import path
from . import views

urlpatterns = [
    path('profile/<int:id>/follow/', views.follow_user, name='follow_user'),
    path('profile/<int:id>/unfollow/', views.unfollow_user, name='unfollow_user'),
]