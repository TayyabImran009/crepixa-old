from django.urls import path

from . import views

app_name = 'orders'
urlpatterns = [
    path('place-your-order/', views.PlaceView.as_view(), name='place'),
    path('order-check/', views.OrderCheckView.as_view(), name='order_check'),
    path('order/', views.OrderView.as_view(), name='order'),
]
