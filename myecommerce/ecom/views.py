from rest_framework.response import Response
from rest_framework.views import APIView
from ecom.models import Coupon
from ecom.api.serializers import CouponSerializer


class CouponAPIView(APIView):
    def get(self, request):
        coupons = Coupon.objects.all()
        serializer = CouponSerializer(coupons, many=True)
        return Response({"coupons":serializer.data})
    