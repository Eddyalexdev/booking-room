from django.urls import path
from . import views

urlpatterns = [
    path('api/booking', views.generate_booking),
]
