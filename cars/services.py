import requests
from rest_framework import status

from config import settings


def current(usd_price):
    response = requests.get(f"{settings.API_URL}v3/latest?apikey={settings.API_KEY}&currencies=RUB")
    if response.status_code == status.HTTP_200_OK:
        current_rub = response.json()["data"]["RUB"]["value"]
        return usd_price * current_rub