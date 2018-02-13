from django.shortcuts import render

# Create your views here.

from .models import MaterialCategory, Material
from fitting.models import FittingCategory, Fitting

def material_cat(request, current_material_category_url_name):
	material_cats = MaterialCategory.objects.all()
	fitting_cats = FittingCategory.objects.all()
	if (current_material_category_url_name == None):
		cur_material_cat = MaterialCategory.objects.all()
		cur_fitting_cat = FittingCategory.objects.all()
	else:
		cur_material_cat = MaterialCategory.objects.filter(url_name=current_material_category_url_name)
		cur_fitting_cat = FittingCategory.objects.filter(url_name=current_material_category_url_name)
	materials = Material.objects.all()
	fittings = Fitting.objects.all()
	return render(request, 'material/material-cat.html', locals())