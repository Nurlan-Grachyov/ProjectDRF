from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from cars.models import Cars, Moto, Milage
from cars.paginators import MotoPaginator
from cars.permissions import OwnerOrStaffOnly
from cars.serialazers import CarSerializer, MotoSerializer, MilageSerializer, MotoMilageSerializer, MotoCreateSerializer
from cars.task import check_milage


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Cars.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer: object) -> None:
        new_moto = serializer.save()
        new_moto.owner = self.request.user
        new_moto.save()


class MotoCreateAPIView(generics.CreateAPIView):
    serializer_class = MotoCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer: object) -> None:
        new_moto = serializer.save()
        new_moto.owner = self.request.user
        new_moto.save()


class MotoListAPIView(generics.ListAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()
    pagination_class = MotoPaginator


class MotoUpdateAPIView(generics.UpdateAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()
    permission_classes = [OwnerOrStaffOnly]


class MotoRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()


class MotoDestroyAPIView(generics.DestroyAPIView):
    queryset = Moto.objects.all()


class MilageCreateApiView(generics.CreateAPIView):
    serializer_class = MilageSerializer

    def perform_create(self, serializer):
        new_milage = serializer.save()
        if new_milage.car:
            check_milage.delay(new_milage.car_id, "Car")
        else:
            check_milage.delay(new_milage.moto_id, "Moto")


class MotoMilageListApiView(generics.ListAPIView):
    queryset = Milage.objects.filter(moto__isnull=False)
    serializer_class = MotoMilageSerializer


class MilageListApiView(generics.ListAPIView):
    serializer_class = MilageSerializer
    queryset = Milage.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('car', 'moto')
    ordering_fields = ('year',)
