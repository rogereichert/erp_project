from django.db.models import Sum, Q, F, Value, IntegerField
from django.db.models.functions import Coalesce

from apps.inventory.models import StockMovement
from apps.products.models import Product


def get_products_with_stock():
    """
    Retorna produtos com informações agregadas de estoque.

    Anota:
    - total_in: total de entradas do produto
    - total_out: total de saídas do produto
    - current_stock: saldo atual em estoque
    """
    return Product.objects.annotate(
        # soma total de entradas do produto
        total_in=Coalesce(
            Sum(
                "stock_movements__quantity",
                filter=Q(
                    stock_movements__movement_type=StockMovement.MovementType.IN
                ),
            ),
            Value(0),
            output_field=IntegerField(),
        ),
        # soma total de saídas do produto
        total_out=Coalesce(
            Sum(
                "stock_movements__quantity",
                filter=Q(
                    stock_movements__movement_type=StockMovement.MovementType.OUT
                ),
            ),
            Value(0),
            output_field=IntegerField(),
        ),
    ).annotate(
        # saldo atual = entradas - saídas
        current_stock=F("total_in") - F("total_out")
    )