from django.urls import path
from . import views

urlpatterns = [
    path('api/booking', views.get_bookings),
    path('api/booking/create', views.create_booking),
]
