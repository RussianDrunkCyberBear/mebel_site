from django.conf.urls import url, include
from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.catalog, {'current_category_url_name' : None},  name='catalog'),
    url(r'^(?P<current_category_url_name>[a-zA-Z0-9_]+)/$', views.catalog, name='catalog', ),

]