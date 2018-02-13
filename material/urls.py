from django.conf.urls import url, include
from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.material_cat, {'current_material_category_url_name' : None},  name='material_cat'),
    url(r'^(?P<current_material_category_url_name>[a-zA-Z0-9_]+)/$', views.material_cat, name='material_cat', ),

]