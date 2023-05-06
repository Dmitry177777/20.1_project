from django.db import models

NULLABLE = {'blank':True, 'null': True}
class Product(models.Model):
    product_name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.CharField(max_length=150, verbose_name='Описание')
    product_image = models.ImageField(upload_to='product_image/', verbose_name='Изображение', **NULLABLE)
    product_category = models.ForeignKey('Category', on_delete=models.CASCADE,)
    product_price = models.IntegerField(verbose_name='Цена за покупку')
    date_of_creation = models.DateField(max_length=150, verbose_name='Дата создания')
    date_of_change = models.DateField(max_length=150, verbose_name='Дата последнего изменения')
    created_at = models.DateTimeField (verbose_name='Время создания', **NULLABLE)
    def __str__(self):
        return f'{self.product_name} {self.description} {self.product_image} {self.product_category} {self.product_price} {self.date_of_creation} {self.date_of_change}'

    class Meta:
        verbose_name='продукция'
        verbose_name_plural='продукции'
        ordering = ('description', )

class Category(models.Model):
    product_category = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.CharField(max_length=150, verbose_name='Описание')


    def __str__(self):
        return f'{self.product_category} {self.description}'

    class Meta:
        verbose_name='категория'
        verbose_name_plural='категории'
        ordering = ('description', )