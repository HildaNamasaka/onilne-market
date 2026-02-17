from django.urls import path
from .views import ProductList, ProductDetail,CategoryDetail, SearchView

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/search/', SearchView.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', ProductDetail.as_view()),
    path('products/<slug:category_slug>/', CategoryDetail.as_view()),
]