from django.urls import path

from . import views
from .views import category_get, main_page

urlpatterns = [
    path("category", views.CategoryViewSet.as_view()),
    path("item", views.ItemViewSet.as_view()),
    path("item_detail", views.ItemDetailViewSet.as_view()),
    path("cards", category_get),
    path("main", main_page, name="main")
]