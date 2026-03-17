from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    """
    Modelo responsável por representar um produto no sistema.

    Utilizado nos pedidos e no controle de estoque.
    O SKU é a principal identificação única do produto.
    """

    class Status(models.TextChoices):
        """
        Status do produto no sistema.

        ACTIVE   → produto disponível para venda
        INACTIVE → produto desativado (não aparece em pedidos)
        """
        ACTIVE = "active", "Ativo"
        INACTIVE = "inactive", "Inativo"

    # código único do produto (muito usado em sistemas ERP)
    sku = models.CharField("SKU", max_length=30, unique=True)

    name = models.CharField("nome", max_length=150)

    # descrição opcional (usado para detalhamento do produto)
    description = models.TextField("descrição", blank=True)

    # uso de Decimal para evitar problemas de precisão financeira
    price = models.DecimalField(
    "preço",
    max_digits=10,
    decimal_places=2,
    validators=[MinValueValidator(Decimal("0.00"))],)

    status = models.CharField(
        "status",
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE,
    )

    # auditoria
    created_at = models.DateTimeField("criado em", auto_now_add=True)
    updated_at = models.DateTimeField("atualizado em", auto_now=True)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ["name"]
        indexes = [
            models.Index(fields=["sku"]),
            models.Index(fields=["status"]),
        ]

    def __str__(self):
        return f"{self.name} ({self.sku})"