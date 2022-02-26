from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

CAR_TYPES = (
    (1, 'Седан'),
    (2, 'Купе'),
    (3, 'Унеревсал'),
    (4, 'Кроссовер'),
)


class Car(models.Model):
    vin = models.CharField(verbose_name='Vin', db_index=True, unique=True, max_length=64)
    color = models.CharField(verbose_name='Color', max_length=64)
    brand = models.CharField(verbose_name='Brand', max_length=64)
    car_type = models.IntegerField(verbose_name='Car-type', choices=CAR_TYPES)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, related_name='car_user')

    class Meta:
        verbose_name = 'Машины'
        ordering = ('id',)

    # def __str__(self):
    #     return f"{self.brand}, -{self.color}"


class Comments(models.Model):
    comment = models.CharField(verbose_name='Комментарий', max_length=64)
    car = models.ForeignKey(Car, verbose_name='Машина', on_delete=models.CASCADE, related_name='car_comment',
                            default=1)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, related_name='com_user',
                             default=1)
