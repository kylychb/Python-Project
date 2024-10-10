from django.shortcuts import render
from rest_framework import generics

from .models import Category, Item
from .serializers import CategorySerializer, ItemSerializer, ItemDetailSerializer


class CategoryViewSet(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ItemViewSet(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetailViewSet(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer

def category_get(request):
    categories = Category.objects.all()
    item = Item.objects.all()
    return render(
        request,
        "cards.html",
        {
            "categories": categories,
            "items": item
        }
    )

# def item_get(request):
#     items = Item.objects.all()