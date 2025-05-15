from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate, APIRequestFactory

from cars.models import Cars
from cars.views import CarViewSet
from users.models import CustomUser


class CarsTest(APITestCase):
    def setUp(self):
        self.owner = CustomUser.objects.create(email="owner@mail")
        self.owner.set_password("12345678")
        self.owner.save()
        self.factory = APIRequestFactory()

        Cars.objects.create(title="test_car", description="car_data", price=100)
        self.car_data = {'title': 'test_car', 'description': 'test_car'}

    def test_create_car(self):
        request = self.factory.post("/cars/", data=self.car_data)
        force_authenticate(request, user=self.owner)
        response = CarViewSet.as_view({'post': 'create'})(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Cars.objects.all().exists())

    def test_list_car(self):
        cars = Cars.objects.all()
        request = self.factory.get("/cars/", json=cars)
        force_authenticate(request, user=self.owner)
        response = CarViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
