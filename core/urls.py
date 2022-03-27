from django.urls import path
from .import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('profiles/<int:pk>/', views.profile_detail_view, name='profile-detail'),
]
