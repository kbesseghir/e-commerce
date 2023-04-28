from django.urls import path 
from . import views 
from .views import *

urlpatterns = [
    path('get/',views.Productcreate.as_view(),name ='get'),
    path('create/',views.Productcreate.as_view(),name ='create'),
    path('get/<int:id>/', views.ProductDetail.as_view(), name=' get product_detail'),
    path('update/<int:id>/', views.ProductDetail.as_view(), name=' update product_detail'),
    path('delete/<int:id>/', views.ProductDetail.as_view(), name=' delete product_detail'),
    path('categories/<str:category>', views.FilterProductsView.as_view(), name='list_categories'),
    path('products/',views.FilterProductsByPrice.as_view(),name='filter_price'),
    path('search/',views.SearchProducts.as_view(),name='Search'),
    path('categories/', CategoryList.as_view(), name='category_list'),
    path('categories/<int:id>/', CategoryDetail.as_view(), name='category_detail'),
    path('categories/<int:id>/products/', CategoryProductList.as_view(), name='category_product_list'),



    
    ]