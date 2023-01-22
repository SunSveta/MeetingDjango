from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    product_name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.CharField(max_length=150, verbose_name='Описание')
    image = models.ImageField(upload_to='products/', verbose_name='Изображение(превью)', **NULLABLE)
    category_id = models.IntegerField(verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за покупку')
    date_create = models.DateTimeField(verbose_name='Дата создания')
    date_update = models.DateTimeField(verbose_name='Дата последнего изменения')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.product_name}, цена {self.price}'


class Category(models.Model):
    category_name = models.CharField(max_length=150, verbose_name='Название категории')
    description = models.TextField(verbose_name='Описание категории')


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'Категория: {self.category_name}, {self.description}'
