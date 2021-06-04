from django.db import models

class Product(models.Model):
    id = models.IntegerField('id', primary_key=True, blank=True)
    title = models.CharField('Название', max_length=60)
    short_disc = models.CharField('Краткое описание', max_length=100)
    price = models.IntegerField('Цена')
    discount_price = models.IntegerField('Цена по скидке', blank=True)
    discount = models.BooleanField('Скидка')
    photo = models.FileField('Фото', upload_to='static/img/')