from django.shortcuts import render

from react_framework.render import Render
from react_framework.decorators import api_view

from .models import Booking
from .serializers import BookingSerializer 

@api_view(['GET'])
def get_bookings(request):
    bookings = Booking.objects.all()
    serializer = BookingSerializer(bookings, many=True)
    return Response({ "tasks": serializer.data })

@api_view(['POST'])
def create_booking(request):
    if Booking.objects.state == 'Pendiente'


