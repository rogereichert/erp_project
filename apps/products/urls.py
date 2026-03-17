# apps/products/urls.py
from django.urls import path
from apps.products.views import (
    ProductListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

# namespace da aplicação para evitar conflitos de URL
app_name = "products"

urlpatterns = [
    # listagem de produtos (com paginação e filtros)
    path("", ProductListView.as_view(), name="list"),

    # criação de novo produto
    path("novo/", ProductCreateView.as_view(), name="create"),

    # edição de produto existente
    path("<int:pk>/editar/", ProductUpdateView.as_view(), name="update"),

    # exclusão de produto com confirmação
    path("<int:pk>/excluir/", ProductDeleteView.as_view(), name="delete"),
]