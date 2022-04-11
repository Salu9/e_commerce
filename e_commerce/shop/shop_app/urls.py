
from django.contrib import admin
from django.urls import path
from . import views
app_name='shop_app'
urlpatterns = [
 path('',views.allProdCat,name='allProdCat'),
 path('<slug:c_slug>/',views.allProdCat,name='products_by_category'),
 path('', views.PrdtDetails, name='PrdtDetails'),
 path('<slug:c_slug>/<slug:product_slug>/', views.PrdtDetails, name='prodCatdetails'),
]