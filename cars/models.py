from heapq import nlargest

from django.db import models
from django.db.models import ForeignKey

from config.settings import AUTH_USER_MODEL


class Cars(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    description = models.CharField(max_length=100, verbose_name='описание')
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True,)

    class Meta:
        verbose_name = 'машина'
        verbose_name_plural = 'машины'


class Moto(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    description = models.CharField(max_length=100, verbose_name='описание')
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True,)

    class Meta:
        verbose_name = 'мотоцикл'
        verbose_name_plural = 'мотоциклы'


class Milage(models.Model):
    milage = models.PositiveIntegerField(verbose_name="пробег")
    year = models.PositiveIntegerField(verbose_name='год регистрации')
    car = ForeignKey(Cars, on_delete=models.CASCADE, null=True, blank=True, related_name='milage')
    moto = ForeignKey(Moto, on_delete=models.CASCADE, null=True, blank=True, related_name='milage')

    def __str__(self):
        return f"{self.moto if self.moto else self.car} - {self.year}"

    class Meta:
        verbose_name = 'пробег'
        verbose_name_plural = 'пробег'
        ordering = ('milage', '-year',)
