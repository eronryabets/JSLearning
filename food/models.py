from django.db import models


class MenuItem(models.Model):
    img = models.ImageField(upload_to='img/tabs/')  # Для хранения изображения меню
    altimg = models.CharField(max_length=100)  # Альтернативный текст изображения
    title = models.CharField(max_length=100)  # Заголовок меню
    descr = models.TextField()  # Описание меню
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Цена меню

    def __str__(self):
        return self.title


class UserRequestInfo(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
