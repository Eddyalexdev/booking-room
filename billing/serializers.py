from rest_framework import serializers
from .models import Billing

class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing
        fields = ['id','proveedor_name', 'proveedor_location', 'proveedor_phone', 'number'] 
