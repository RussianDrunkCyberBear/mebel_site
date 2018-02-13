from django.contrib import admin

# Register your models here.

from .models import MaterialCategory, Material



class MaterialCategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'url_name', 'id']
	readonly_fields=('url_name',)

admin.site.register(MaterialCategory, MaterialCategoryAdmin)



class MaterialAdmin(admin.ModelAdmin):
	list_display = ['name', 'category', 'material_image', 'id']
	list_filter = ['category']
	list_editable = ['category']

admin.site.register(Material, MaterialAdmin)