from django.urls import path
from ecom import views


app_name = 'ecom'

urlpatterns = [
    path('coupons/', views.CouponAPIView.as_view(), name='CouponAPIView'),
 ]