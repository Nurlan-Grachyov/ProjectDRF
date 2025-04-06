from django.urls import path

from rest_framework.routers import DefaultRouter

from cars.apps import CarsConfig
from cars.views import CarViewSet, MotoListAPIView, MotoCreateAPIView, MotoUpdateAPIView, MotoRetrieveAPIView, \
    MotoDestroyAPIView, MilageCreateApiView, MotoMilageListApiView, MilageListApiView

app_name = CarsConfig.name

router = DefaultRouter()
router.register(r'cars', CarViewSet, basename='cars')
urlpatterns = [
                  path('moto/', MotoListAPIView.as_view(), name='list_moto'),
                  path('create_moto/', MotoCreateAPIView.as_view(), name='create_moto'),
                  path('update_moto/<int:pk>/', MotoUpdateAPIView.as_view(), name='update_moto'),
                  path('retrieve_moto/<int:pk>/', MotoRetrieveAPIView.as_view(), name='retrieve_moto'),
                  path('destroy_moto/<int:pk>/', MotoDestroyAPIView.as_view(), name='destroy_moto'),

                  path('create_milage/', MilageCreateApiView.as_view(), name='create_milage'),
                  path('moto_milage/', MotoMilageListApiView.as_view(), name='moto_milage'),
                  path('milage/', MilageListApiView.as_view(), name='milage'),
              ] + router.urls
