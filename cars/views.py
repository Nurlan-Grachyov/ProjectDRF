from rest_framework import viewsets, generics

from cars.models import Cars, Moto
from cars.serialazers import CarSerializer, MotoSerializer


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Cars.objects.all()


class MotoCreateAPIView(generics.CreateAPIView):
    serializer_class = MotoSerializer


class MotoListAPIView(generics.ListAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()


class MotoUpdateAPIView(generics.UpdateAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()


class MotoRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()


class MotoDestroyAPIView(generics.DestroyAPIView):
    queryset = Moto.objects.all()
