from django.urls import path
from . import views

urlpatterns = [
    path('post_form/', views.create_post, name='post_form'),
    path('post_list/', views.post_list, name='post_list'),
    path('post_detail/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post_detail/<int:post_id>/edit', views.edit_post, name='edit_post'),
    path('post_detail/<int:post_id>/delete', views.delete_post, name='delete_post'),
]