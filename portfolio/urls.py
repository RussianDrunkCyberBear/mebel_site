from django.conf.urls import url, include
from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.portfolio_cat, name='portfolio_cat'),
    url(r'^(?P<portfolio_id>[0-9]+)/$', views.portfolio_card, name='portfolio_id'),
]