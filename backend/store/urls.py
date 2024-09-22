from django.urls import path

from .views import CategoryListView, ProductListView

urlpatterns = [
    path("api/categories/", CategoryListView.as_view(), name="category-list"),
    path("api/products/", ProductListView.as_view(), name="product-list"),
]
