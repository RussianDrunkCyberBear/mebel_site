from django.contrib import admin

from .models import FittingCategory, Fitting



class FittingCategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'url_name', 'id']
	readonly_fields=('url_name',)

admin.site.register(FittingCategory, FittingCategoryAdmin)



class FittingAdmin(admin.ModelAdmin):
	list_display = ['name', 'category', 'fitting_image', 'id']
	list_filter = ['category']
	list_editable = ['category']

admin.site.register(Fitting, FittingAdmin)
