from django.urls import path
from apps.customers.views import (
    CustomerListView,
    CustomerCreateView,
    CustomerUpdateView,
    CustomerDeleteView,
)

app_name = "customers"  # namespace para evitar conflitos de nomes em URLs


urlpatterns = [
    # listagem de clientes (com paginação e busca)
    path("", CustomerListView.as_view(), name="list"),

    # criação de novo cliente
    path("novo/", CustomerCreateView.as_view(), name="create"),

    # edição de cliente existente (via PK)
    path("<int:pk>/editar/", CustomerUpdateView.as_view(), name="update"),

    # exclusão de cliente com confirmação
    path("<int:pk>/excluir/", CustomerDeleteView.as_view(), name="delete"),
]