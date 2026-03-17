from django.core.exceptions import ValidationError
from django.db import transaction

from apps.inventory.models import StockMovement
from apps.orders.models import Order


@transaction.atomic
def confirm_order(order: Order) -> None:
    """
    Confirma um pedido em rascunho.

    Regras aplicadas:
    - somente pedidos em rascunho podem ser confirmados
    - todos os itens devem possuir estoque suficiente
    - ao confirmar, são geradas movimentações de saída no estoque
    - o status final do pedido passa para confirmado
    """
    if order.status != Order.Status.DRAFT:
        raise ValidationError("Somente pedidos em rascunho podem ser confirmados.")

    items = list(order.items.select_related("product").all())

    if not items:
        raise ValidationError("Não é possível confirmar um pedido sem itens.")

    for item in items:
        if item.product.current_stock < item.quantity:
            raise ValidationError(
                f"Estoque insuficiente para o produto {item.product.name}."
            )

    for item in items:
        StockMovement.objects.create(
            product=item.product,
            movement_type=StockMovement.MovementType.OUT,
            quantity=item.quantity,
            note=f"Saída referente ao pedido #{order.pk}",
        )

    order.status = Order.Status.CONFIRMED
    order.save(update_fields=["status", "updated_at"])