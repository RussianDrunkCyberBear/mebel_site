from django.conf.urls import url, include
from django.conf.urls import url, include

from . import views

urlpatterns = [
    # url(r'^$', views.product_card, { 'product_id' : 0}, name='product_card'),
    url(r'^(?P<product_id>[0-9]+)/$', views.product_card, name='product_card'),
]