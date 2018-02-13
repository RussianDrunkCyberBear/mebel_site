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
    in_stock = models.BooleanField(default=False, verbose_name='Товар по акции')
    stock_descript = models.ForeignKey('ProductStock', blank=True, null=True, verbose_name='Акция')
    # main_image = models.ForeignKey('ProductImage', blank=True, null=True, default=None, related_name="main_image", verbose_name="Основное изображение")
    main_image = models.ImageField(null=True, upload_to=prod_mainimage_upload_path)
    description = models.TextField(blank=True, verbose_name='Полное описание')
    category = models.ForeignKey(Category, blank=True, null=True, default=None, verbose_name='Категория', on_delete=models.SET_NULL)
    # price = models.DecimalField (max_digits=10, decimal_places=2, default=0, verbose_name='Цена')
    length = models.CharField(max_length=8, blank=True, verbose_name='Длина, мм')
    width = models.CharField(max_length=8, blank=True, verbose_name='Ширина, мм')
    height = models.CharField(max_length=8, blank=True, verbose_name='Высота, мм')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    # materials_face = models.ManyToManyField(Material, blank=True, related_name='mat_face', verbose_name='Доступные материалы фасада')
    materials_face = models.TextField(blank=True, verbose_name='Материал')
    materials_deck = models.TextField(blank=True, verbose_name='Столешница')
    # materials_deck = models.ManyToManyField(Material, blank=True, related_name='mat_deck', verbose_name='Доступные материалы столешницы')
    # materials_coat = models.ManyToManyField(Material, blank=True, related_name='mat_coat', verbose_name='Доступные материалы обивки')
    # materials_others = models.ManyToManyField(Material, blank=True, related_name='mat_others', verbose_name='Доступные материалы прочие')
    materials_text = models.TextField(blank=True, verbose_name='Другие материалы')
    # fitting_1 = models.ManyToManyField(Fitting, blank=True, related_name='fit_1', verbose_name='Фурнитура_1')
    # fitting_2 = models.ManyToManyField(Fitting, blank=True, related_name='fit_2', verbose_name='Фурнитура_2')
    # fitting_3 = models.ManyToManyField(Fitting, blank=True, related_name='fit_3', verbose_name='Фурнитура_3')
    # fitting_4 = models.ManyToManyField(Fitting, blank=True, related_name='fit_4', verbose_name='Фурнитура_4')

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