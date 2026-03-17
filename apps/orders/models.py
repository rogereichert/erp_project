from django.db import models
from decimal import Decimal
from apps.customers.models import Customer


class Order(models.Model):
    """
    Modelo principal de pedido.

    Representa o cabeçalho do pedido, vinculado a um cliente.
    Os produtos e valores ficam nos itens do pedido.
    """

    class Status(models.TextChoices):
        """
        Status do ciclo de vida do pedido.

        DRAFT     → pedido em montagem, ainda editável
        CONFIRMED → pedido finalizado e validado
        CANCELED  → pedido cancelado
        """
        DRAFT = "draft", "Rascunho"
        CONFIRMED = "confirmed", "Confirmado"
        CANCELED = "canceled", "Cancelado"

    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,  # preserva o histórico de pedidos
        related_name="orders",
        verbose_name="cliente",
    )

    status = models.CharField(
        "status",
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
    )

    # campos de auditoria
    created_at = models.DateTimeField("criado em", auto_now_add=True)
    updated_at = models.DateTimeField("atualizado em", auto_now=True)

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["customer"]),
            models.Index(fields=["status"]),
            models.Index(fields=["created_at"]),
        ]

    def __str__(self):
        return f"Pedido #{self.pk}"

    @property
    def total_amount(self):
        """
        Retorna o valor total do pedido com base na soma dos itens.
        """
        return sum((item.total_price for item in self.items.all()), Decimal("0.00"))