from rest_framework import status
from rest_framework.test import APITestCase

from cars.models import Cars


class CarsTest(APITestCase):
    def setUp(self):
        pass

    def test_create_car(self):
        car_data = {'title': 'test_car', 'description': 'test_car'}
        response = self.client.post("/cars/", json=car_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.json(),
                         {"id": 1, "milage": [], "title": "test_car", "description": "test_car", "owner": None})

        self.assertTrue(Cars.objects.all().exists())

    def list_test_car(self):
        cars = Cars.objects.create(title="test_list_car", descroption='test_list_car')

        response = self.client.post("/cars/", json=cars)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.json(),
                         [{"id": 1, "milage": [], "title": "test_car", "description": "test_car", "owner": None}])
