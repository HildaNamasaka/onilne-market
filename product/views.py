from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, Category

from rest_framework import generics, filters, status

from .serializer import ProductSerializer, CategorySerializer

# Create your views here.

class SearchView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description', 'category__name']
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if not queryset.exists():
            return Response(
                {
                'message': f'No results for "{request.GET.get("search")}"',
                },
                status= status.HTTP_404_NOT_FOUND
                )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
        
class ProductList(APIView):
    def get(self, request, format=None):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
    
class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug ):
        try:
            return Product.objects.filter(category__slug = category_slug).get(slug = product_slug)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request,category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug = category_slug)
        except Category.DoesNotExist:
            raise Http404
        
    def get(self, request, category_slug, format=None):
        category  = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)