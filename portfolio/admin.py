from django.contrib import admin
from .models import PortfolioItem, PortfolioImage
from django import forms

# Register your models here.


class PortfolioImageAdmin (admin.ModelAdmin):
	list_display = ['id','prfol_product','is_active', 'image']
	list_filter = ['prfol_product', 'is_active']

	class Meta:
		model = PortfolioImage

admin.site.register(PortfolioImage, PortfolioImageAdmin)


class ItemMainImageForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(ItemMainImageForm, self).__init__(*args, **kwargs)
		self.fields['main_image'].queryset = PortfolioImage.objects.filter(prfol_product=self.instance)	#для того чтобы основной фотографией можно было поставить только из тех что принадлежат товару
		self.fields['main_image'].label_from_instance = lambda obj: "%s" % (obj.image)


class PortfolioImageInline (admin.TabularInline):
	model = PortfolioImage

class PortfolioItemAdmin (admin.ModelAdmin):
	list_display = ['name','id', 'is_active',]
	list_editable = ['is_active',]
	inlines = [PortfolioImageInline,]
	form = ItemMainImageForm

	class Meta:
		model = PortfolioItem

admin.site.register(PortfolioItem, PortfolioItemAdmin)