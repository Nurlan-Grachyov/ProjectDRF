from rest_framework import status
from rest_framework.test import APITestCase

from cars.models import Cars


class CarsTest(APITestCase):
    def setUp(self):
        pass

    def test_create_car(self):
        car = Cars.objects.create(title='test_car', description='test_car')
        response = self.client.post("cars/", data=car)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)