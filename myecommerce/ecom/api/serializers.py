from rest_framework import serializers
from ecom.models import Coupon, Product

class CouponSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    code = serializers.CharField(max_length=10)
    discount= serializers.ImageField()
    active = serializers.BooleanField()

    
