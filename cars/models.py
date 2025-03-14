from django.db import models

class Cars(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    description = models.CharField(max_length=100, verbose_name='описание')

    class Meta:
        verbose_name = 'машина'
        verbose_name_plural = 'машины'


class Moto(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    description = models.CharField(max_length=100, verbose_name='описание')

    class Meta:
        verbose_name = 'мотоцикл'
        verbose_name_plural = 'мотоциклы'