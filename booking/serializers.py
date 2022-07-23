from react_framework import serializers
from .models import Booking

from room.serializers import RoomSerializer

class BookingSerializer(serializers.ModelSerializer):
    room = RoomSerializer()

    class Meta:
        model = Booking
        fields = ['id', 'room']
