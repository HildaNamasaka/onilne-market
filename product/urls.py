from django.urls import path
from .views import ProductList, ProductDetail

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
    path('details/<slug:category_slug>/<slug:product_slug>/', ProductDetail.as_view(), name='product-details')
]