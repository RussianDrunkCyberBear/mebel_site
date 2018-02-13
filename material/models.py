from django.db import models
from mebel.my_func import transliterate

# Create your models here.

class MaterialCategory(models.Model):
	name = models.CharField(max_length=24, verbose_name='Название категории')
	url_name = models.CharField(max_length=40, blank=True, null=True, default='')

	def __str__(self):
		return '%s'% self.name
	
	class Meta:
		verbose_name = 'Категория материалов'
		verbose_name_plural = 'Категории материалов'

	def save(self, *args, **kwargs):    #вычисляет поле url_name из значения поля имени
		super(MaterialCategory, self).save(*args, **kwargs) # Call the "real" save() method.
		self.url_name = 'materialid'+ str(self.id) + '_' + transliterate(self.name)
		super(MaterialCategory, self).save(*args, **kwargs) # Call the "real" save() method.



class Material(models.Model):
	name = models.CharField(max_length=48, verbose_name='Название материала')
	material_image = models.ImageField(upload_to='material_images', default='default/NO_IMAGE.png')
	category = models.ForeignKey(MaterialCategory, verbose_name='Категория материала', blank=True, null=True, default=None)

	def __str__(self):
		return '%s: %s'% (self.category.name, self.name)

	class Meta:
		verbose_name = 'Материал'
		verbose_name_plural = 'Материалы'
