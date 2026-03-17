from django.db import models
from apps.products.models import Product


class StockMovement(models.Model):
    """
    Modelo responsável por registrar todas as movimentações de estoque.

    O estoque não é armazenado diretamente no produto, mas calculado
    com base no histórico de entradas e saídas (modelo de ledger).
    """

    class MovementType(models.TextChoices):
        """
        Tipos de movimentação de estoque.

        IN  → entrada de produtos (compra, ajuste positivo)
        OUT → saída de produtos (venda, perda, ajuste negativo)
        """
        IN = "in", "Entrada"
        OUT = "out", "Saída"

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,  # impede exclusão de produto com histórico
        related_name="stock_movements",
        verbose_name="produto",
    )

    movement_type = models.CharField(
        "tipo de movimentação",
        max_length=10,
        choices=MovementType.choices,
    )

    # quantidade sempre positiva; o tipo define entrada ou saída
    quantity = models.PositiveIntegerField("quantidade")

    # campo opcional para observações (ex: "ajuste manual", "pedido #123")
    note = models.CharField("observação", max_length=255, blank=True)

    created_at = models.DateTimeField("criado em", auto_now_add=True)

    class Meta:
        verbose_name = "Movimentação de estoque"
        verbose_name_plural = "Movimentações de estoque"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["product"]),
            models.Index(fields=["movement_type"]),
            models.Index(fields=["created_at"]),
        ]

    def __str__(self):
        return f"{self.product.name} - {self.movement_type} - {self.quantity}"