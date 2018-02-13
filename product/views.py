from django.shortcuts import render

# Create your views here.

from product.models import Category, Product, ProductImage

from catalog.views import *

from material.models import Material


def product_card(request, product_id):
	categories = Category.objects.all()

	if (Product.objects.filter(id=product_id, is_active=True).exists() == True):
		product = Product.objects.get(id=product_id)
		prod_main_image = product.main_image
		prod_images = ProductImage.objects.filter(product=product, is_active=True)
		# mat_face = product.materials_face.all()
		# mat_deck = product.materials_deck.all()
		# mat_coat = product.materials_coat.all()
		# mat_others = product.materials_others.all()
		mat_face = product.materials_face
		mat_deck = product.materials_deck
		mat_text = product.materials_text
		# fit_1 = product.fitting_1.all()
		# fit_2 = product.fitting_2.all()
		# fit_3 = product.fitting_3.all()
		# fit_4 = product.fitting_4.all()
		products_in_cat = Product.objects.filter(category=product.category).exclude(id=product.id)[:20]
		
		if (product.category != None):
			cur_cat = Category.objects.get(id=product.category.id)
			cur_cat_url_name = cur_cat.url_name
			path = calc_path(cur_cat.id)
		else:
			cur_cat = None
			cur_cat_url_name = None

	cur_lvl = current_cat_lvl(cur_cat_url_name)
	tree = tree_cat_list(cur_cat_url_name, cur_lvl)


	return render(request, 'product/product_card.html', locals())