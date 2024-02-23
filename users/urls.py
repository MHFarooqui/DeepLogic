from django.urls import path
from users import views

urlpatterns = [
    path('users/login', views.userLogin),
    path('posts/', views.get_posts),
    path('posts/create', views.create_post)
]