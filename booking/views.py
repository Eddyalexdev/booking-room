from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Booking
from .serializers import BookingSerializer

from room.models import Room

@api_view(['GET'])
def get_bookings(request):
    bookings = Booking.objects.all()
    serializer = BookingSerializer(bookings, many=True)
    return Response({ "tasks": serializer.data })

@api_view(['POST'])
def create_booking(request):
    user = request.data['user']
    id_room = request.data['room']
    state = request.data['state']
    room = Room.objects.get(id=id_room)

    if room.avaiable == True:
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(status=status.HTTP_404_NOT_FOUND)


