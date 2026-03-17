# apps/core/views.py
from django.views.generic import TemplateView

from apps.customers.models import Customer
from apps.orders.models import Order
from apps.products.models import Product


class DashboardView(TemplateView):
    """
    View responsável por exibir o dashboard principal do sistema.

    Centraliza métricas gerais do ERP para exibição na página inicial.
    """
    template_name = "core/dashboard.html"

    def get_context_data(self, **kwargs):
        """
        Adiciona ao contexto os principais indicadores do sistema:
        - total de clientes
        - total de produtos
        - total de pedidos
        - total de pedidos confirmados
        - últimos pedidos realizados
        """
        context = super().get_context_data(**kwargs)

        # métricas gerais para os cards do dashboard
        context["total_customers"] = Customer.objects.count()
        context["total_products"] = Product.objects.count()
        context["total_orders"] = Order.objects.count()
        context["confirmed_orders"] = Order.objects.filter(
            status=Order.Status.CONFIRMED
        ).count()

        # últimos pedidos com cliente carregado para evitar consultas extras no template
        context["latest_orders"] = Order.objects.select_related("customer")[:5]

        return context