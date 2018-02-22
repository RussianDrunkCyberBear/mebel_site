from django.db import models
from mebel.my_func import transliterate
import os
from mebel import settings
from material.models import Material
from fitting.models import Fitting


class Category(models.Model):
    name = models.CharField(max_length=24, verbose_name='Наименование категории')
    parent_cat = models.ForeignKey('self', blank=True, null=True, default=None, verbose_name='Является подкатегорией:', on_delete=models.SET_NULL)
    url_name = models.CharField(max_length=32, blank=True, null=True, default='')
    image = models.ImageField(upload_to='category_images', default='default/NO_IMAGE.png')

    def __str__(self):
        return '%s'% self.name

    class Meta:
        verbose_name='Категория товара'
        verbose_name_plural='Категории товаров'

    def save(self, *args, **kwargs):    #вычисляет поле url_name из значений других полей
        super(Category, self).save(*args, **kwargs)
        self.url_name = 'catid'+ str(self.id) + '_' + transliterate(self.name)
        super(Category, self).save(*args, **kwargs) # Call the "real" save() method.



def prod_mainimage_upload_path (instance, filename):
    return 'product_images/prodid_{0}/{1}'.format(instance.id, filename)

class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    on_main_page = models.BooleanField(default=False, verbose_name='Показывать на главной')
    in_portfolio = models.BooleanField(default=False, verbose_name='Товар из портфолио (показывать в начале каталога)')
    in_stock = models.BooleanField(default=False, verbose_name='Товар по акции')
    stock_descript = models.ForeignKey('ProductStock', blank=True, null=True, verbose_name='Акция')
    main_image = models.ImageField(null=True, upload_to=prod_mainimage_upload_path)
    description = models.TextField(blank=True, verbose_name='Полное описание')
    category = models.ForeignKey(Category, blank=True, null=True, default=None, verbose_name='Категория', on_delete=models.SET_NULL)
    length = models.CharField(max_length=8, blank=True, verbose_name='Длина, мм')
    width = models.CharField(max_length=8, blank=True, verbose_name='Ширина, мм')
    height = models.CharField(max_length=8, blank=True, verbose_name='Высота, мм')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    materials_face = models.TextField(blank=True, verbose_name='Материал')
    materials_deck = models.TextField(blank=True, verbose_name='Столешница')
    materials_text = models.TextField(blank=True, verbose_name='Другие материалы')

    def __str__(self):
        return '%s'% self.name

    class Meta:
        verbose_name='Товар'
        verbose_name_plural='Товары'


def prod_image_upload_path (instance, filename):
    return 'product_images/prodid_{0}/{1}'.format(instance.product.id, filename)


class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    image = models.ImageField(upload_to=prod_image_upload_path)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Изображение товара"
        verbose_name_plural = "Изображения товара"

    def __str__(self):
        return '%s' % self.product

    def delete(self, *args, **kwargs):
        super(ProductImage, self).delete(*args, **kwargs)
        os.remove(os.path.join(settings.MEDIA_ROOT, self.image.name))


class ProductStock(models.Model):
    descript = models.TextField(blank=True, verbose_name='Описание акции')
    is_active = models.BooleanField(default=True, verbose_name='Активна')

    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = "Акции"

    def __str__(self):
        return '%s' % self.descript