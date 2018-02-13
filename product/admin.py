from django.contrib import admin
from django import forms

# Register your models here.

from .models import Product, Category, ProductImage, ProductStock


class ProductImageInline (admin.TabularInline):
	model = ProductImage

class ProductImageAdmin (admin.ModelAdmin):
	list_display = ['id','image', 'product','is_active',]
	list_filter = ['product', 'is_active']

	class Meta:
		model = ProductImage

admin.site.register(ProductImage, ProductImageAdmin)


class ItemMainImageForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(ItemMainImageForm, self).__init__(*args, **kwargs)
		self.fields['main_image'].queryset = ProductImage.objects.filter(product=self.instance)	#для того чтобы основной фотографией можно было поставить только из тех что принадлежат товару
		self.fields['main_image'].label_from_instance = lambda obj: "%s" % (obj.image)


class ProductAdmin (admin.ModelAdmin):
	list_display = ['name','id', 'is_active', 'category', 'in_stock', 'on_main_page',]
	list_filter = ['is_active', 'category', 'in_stock', 'on_main_page',]
	list_editable = ['is_active', 'category', 'in_stock', 'on_main_page',]
	# filter_horizontal = ('materials_face', 'materials_deck', 'materials_coat', 'materials_others', 'fitting_1', 'fitting_2', 'fitting_3', 'fitting_4',)
	inlines = [ProductImageInline,]
	form = ItemMainImageForm

	class Meta:
		model = Product

admin.site.register(Product, ProductAdmin)




from django.db.models import Q
from django import forms

class CategoryForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(CategoryForm, self).__init__(*args, **kwargs)
		self.fields['parent_cat'].queryset = Category.objects.filter(~Q(id=self.instance.id))	#для того чтобы невозможно было сделать кактeгорию родителем самой себе она исключается из выборки


class CategoryInline (admin.TabularInline):
	model = Category
	readonly_fields=('url_name',)
	extra = 1


class CategoryAdmin (admin.ModelAdmin):
	list_display = ['name','get_path','parent_cat','url_name','id']
	list_filter = ['parent_cat']
	list_display_links = ['name']
	readonly_fields=('url_name',)
	inlines = [CategoryInline,]
	form = CategoryForm

	class Meta:
		model = Category


	def get_path(self, obj):	#для отображения дерева каталога ввиде cat0/cat01/cat001/....	для понимания структуры каталога
		cat_path = ''
		current_obj_parent = obj.parent_cat
		# for i in range (0, 10):	
		# 	if (current_obj_parent == None):
		# 		break
		# 	cat_path = str(current_obj_parent) + '/' + cat_path
		# 	current_obj_parent = current_obj_parent.parent_cat
		i = 0	#для предотвращения бесконечного цикла
		while (current_obj_parent != None):			#цикл проходит по полю родителская_категория до верхнего уровня каталога
			cat_path = str(current_obj_parent) + '/' + cat_path
			current_obj_parent = current_obj_parent.parent_cat
			i += 1
			if (i > 10):
				return '!RECURSIVE ERROR! ' +'--/' + cat_path
		return '--/' + cat_path


admin.site.register(Category, CategoryAdmin)


@admin.register(ProductStock)
class ProductStockAdmin(admin.ModelAdmin):
	list_display = ['descript', 'is_active']
	list_editable = ['is_active']
	list_filter = ['is_active']

