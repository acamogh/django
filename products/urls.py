from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
     url(r'^contact/', views.contact, name='contact'),
     url(r'^$', views.ProductViewList.as_view(), name='ProductViewList'),
     url(r'^(?P<pk>\d+)/$', views.ProductDetailView.as_view(), name='Product_Detail'),
     url(r'^(?P<pk>\d+)/inventory/$', views.VariationListView.as_view(), name='product_inventory'),

]
