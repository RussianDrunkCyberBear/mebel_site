from django.shortcuts import render
from product.models import Category, Product, ProductImage

# Create your views here.

def catalog(request, current_category_url_name):
	categories = Category.objects.all()
	# categories = Category.objects.filter(parent_cat=None)
	if (current_category_url_name != None):
		cur_cat = Category.objects.get(url_name = current_category_url_name)
		path = calc_path(cur_cat.id)		# получаем иерахический список родительских категорий в виде списка объектов (похоже на qeryset)
		products = Product.objects.filter(category=cur_cat, is_active=True)
		if ( ("Kuhni" in current_category_url_name) and (cur_cat.parent_cat == None) ):
			products = Product.objects.filter(category__parent_cat__url_name__contains="Kuhni", is_active=True)
	else: 
		# products = Product.objects.filter(category=None, is_active=True)
		products = Product.objects.filter(is_active=True)
	cur_lvl = current_cat_lvl(current_category_url_name)
	tree = tree_cat_list(current_category_url_name, cur_lvl)
	return render(request, 'catalog.html', locals())


def calc_path(cur_cat_id):							# проходим по полям parent_cat, доходя до None, получяя список категорий ввиде пути 
	cur_obj = Category.objects.get(id=cur_cat_id)	# в список сохраняются объекты, чтобы иметь доступ к их полям (название, ссылки)
	path = [cur_obj]
	i = 0
	while (cur_obj.parent_cat != None):
		i += 1
		if (i > 10):
			return ['!RECURSIVE ERROR! ']
		path.insert(0, cur_obj.parent_cat)
		cur_obj = Category.objects.get(id=cur_obj.parent_cat.id)
	return path


def tree_cat_list (cur_cat_url, lvl):
	tree_list = []
	i = 0
	if cur_cat_url is None:			#если верхний уровень каталога возвращает список каткгорий первого уровня
		for instanse in Category.objects.filter(parent_cat=None):
			tree_list.append([instanse, ''])
		return tree_list
	else:
		cur_cat = Category.objects.get(url_name = cur_cat_url)	
		pre_parent = None
		while(i<10):	#защита от бесконечности	
			i += 1
			cur_list = []
			for instanse in Category.objects.filter(parent_cat=cur_cat.id):
				cur_list.append([instanse, lvl])
				if ((instanse == pre_parent) and (pre_parent is not None)):
					for pre_isnst in pre_list:
						cur_list.append(pre_isnst)
			pre_parent = cur_cat
			if (cur_cat.parent_cat == None):
				for instanse in Category.objects.filter(parent_cat=None):
					tree_list.append([instanse, ''])
					if (pre_parent == instanse):
						for cur_isnst in cur_list:
							tree_list.append(cur_isnst)
				break
			cur_cat = Category.objects.get(id=cur_cat.parent_cat.id)
			pre_list = cur_list
			# lvl -= 1
			lvl = lvl[0:-2]

	return tree_list

def current_cat_lvl (cat_url_name):
	# level = 0
	level = ''
	if (cat_url_name == None):
		return level
	else:
		# level += 1
		level += '--'
		cur_cat = Category.objects.get(url_name = cat_url_name)
		while (cur_cat.parent_cat != None):
			cur_cat = Category.objects.get(id=cur_cat.parent_cat.id)
			# level += 1
			level += '--'
		return level





# def tree_cat_list (cur_cat_url):
# 	tree_list = []
# 	i = 0
# 	if cur_cat_url is None:			#если верхний уровень каталога возвращает список каткгорий первого уровня
# 		for instanse in Category.objects.filter(parent_cat=None):
# 			tree_list.append(instanse)
# 		return tree_list
# 	else:
# 		cur_cat = Category.objects.get(url_name = cur_cat_url)	
# 		pre_parent = None
# 		while(i<10):	#защита от бесконечности	
# 			i += 1
# 			cur_list = []
# 			for instanse in Category.objects.filter(parent_cat=cur_cat.id):
# 				cur_list.append(instanse)
# 				if ((instanse == pre_parent) and (pre_parent is not None)):
# 					cur_list.append(pre_list)
# 			pre_parent = cur_cat
# 			if (cur_cat.parent_cat == None):
# 				for instanse in Category.objects.filter(parent_cat=None):
# 					tree_list.append(instanse)
# 					if (pre_parent == instanse):
# 						tree_list.append(cur_list)
# 				break
# 			cur_cat = Category.objects.get(id=cur_cat.parent_cat.id)
# 			pre_list = cur_list

# 	return tree_list	

def unnest_list (n_list):
	i = 0
	while (i<len(n_list)):
		if isinstance(n_list[i], list):
			for k in range(len(n_list[i])-1 ,-1, -1):
				n_list.insert(i+1, n_list[i][k])
				n_list[i].pop(k)
			n_list.pop(i)
		i += 1
	return n_list


def leveled_list (n_list, lvl=0):
	for i in range (0, len(n_list)):
		if (type(n_list[i]) is list):
			leveled_list(n_list[i], lvl+1)
			#n_list.pop(i)
			#n_list.insert(i, 'is_list')
		else:
			n_list.insert(i, [n_list[i], lvl])
			n_list.pop(i+1)
	return n_list

