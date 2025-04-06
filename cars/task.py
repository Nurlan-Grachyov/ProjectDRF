from celery import shared_task

from cars.models import Moto, Cars


@shared_task
def check_milage(pk, model):
    if model == "Car":
        instance = Cars.objects.filter(pk=pk).first()
    else:
        instance = Moto.objects.filter(pk=pk).first()

    if instance:
        prev_milage = -1
        for m in instance.milage.all():
            if prev_milage == -1:
                prev_milage = m.milage

            else:
                if prev_milage < m.milage:
                    print("Неверный пробег")
                    break

def check_filter():
    filter_price = {"price__lte": 500}
    if Cars.objects.filter(**filter_price).exists():
        print("Получены отфильтрованные машины")

