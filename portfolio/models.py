from django.db import models
from .models import *

# Create your models here.

class PortfolioItem(models.Model):
    name = models.CharField(max_length=24, verbose_name='Наименование работы')
    is_active = models.BooleanField(default=True)
    description = models.TextField(blank=True, verbose_name='Описание')
    main_image = models.ForeignKey('PortfolioImage', blank=True, null=True, default=None, verbose_name="Основное изображение")

    def __str__(self):
        return '%s'% self.name

    class Meta:
        verbose_name='Товар в портфолио'
        verbose_name_plural='Товары в портфолио'

def portf_image_upload_path (instance, filename):
    return 'portfolio_images/portfid_{0}/{1}'.format(instance.prfol_product.id, filename)


class PortfolioImage(models.Model):
    prfol_product = models.ForeignKey(PortfolioItem, blank=True, null=True, default=None)
    image = models.ImageField(upload_to=portf_image_upload_path)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Изображение товара в портфолио"
        verbose_name_plural = "Изображения товара в портфолио"

    def __str__(self):
        return '%s' % self.prfol_product