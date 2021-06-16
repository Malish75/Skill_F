from django.db import models
from datetime import datetime


class Appointment(models.Model):
    date = models.DateField(
        default=datetime.utcnow,
    )
    client_name = models.CharField(
        max_length=200
    )
    message = models.TextField()

    def __str__(self):
        return f'{self.client_name}: {self.message}'

'''Это модель записи на приём к кому угодно.
 Давайте будем думать, что это запись на приём к врачу. Здесь есть сообщение от пользователя, его имя и дата записи.'''