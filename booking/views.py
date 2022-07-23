from django.shortcuts import render

from react_framework.render import Render
from react_framework.decorators import api_view

@api_view(['POST'])
def generate_booking(request):

