import requests
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from rest_framework import status

from config import settings


def current(usd_price):
    response = requests.get(f"{settings.API_URL}v3/latest?apikey={settings.API_KEY}&currencies=RUB")
    if response.status_code == status.HTTP_200_OK:
        current_rub = response.json()["data"]["RUB"]["value"]
        rub_price = usd_price * current_rub
        return rub_price
    else:
        return None

def set_schedule():
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=10,
        period=IntervalSchedule.SECONDS,
    )

    PeriodicTask.objects.create(
        interval=schedule,
        name='Check filter',
        task='cars.tasks.check_filter',
    )
