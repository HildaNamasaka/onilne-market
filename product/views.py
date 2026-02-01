from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product

from .serializer import ProductSerializer

# Create your views here.

class ProductList(APIView):
    def get(self, request, format=None):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)