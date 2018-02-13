from django.db import models
from mebel.my_func import transliterate



class FittingCategory(models.Model):
	name = models.CharField(max_length=24, verbose_name='Название категории')
	url_name = models.CharField(max_length=40, blank=True, null=True, default='')

	def __str__(self):
		return '%s'% self.name
	
	class Meta:
		verbose_name = 'Категория фурнитуры'
		verbose_name_plural = 'Категории фурнитуры'

	def save(self, *args, **kwargs):    #вычисляет поле url_name из значения поля имени
		super(FittingCategory, self).save(*args, **kwargs) # Call the "real" save() method.
		self.url_name = 'fittcatid'+ str(self.id) + '_' + transliterate(self.name)
		super(FittingCategory, self).save(*args, **kwargs) # Call the "real" save() method.



class Fitting(models.Model):
	name = models.CharField(max_length=48, verbose_name='Название предмета')
	fitting_image = models.ImageField(upload_to='fitting_images', default='default/NO_IMAGE.png')
	category = models.ForeignKey(FittingCategory, verbose_name='Категория фурнитуры', blank=True, null=True, default=None)

	def __str__(self):
		return '%s: %s'% (self.category.name, self.name)

	class Meta:
		verbose_name = 'Предмет фурнитуры'
		verbose_name_plural = 'Предметы фурнитуры'
