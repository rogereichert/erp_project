from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # Core (dashboard)
    path("", include("apps.core.urls")),

    # Customers
    path("clientes/", include("apps.customers.urls")),

    # Products
    path("produtos/", include("apps.products.urls")),

    # Orders
    #path("pedidos/", include("apps.orders.urls")),

    # Inventory
    #path("estoque/", include("apps.inventory.urls")),
]