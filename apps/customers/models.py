from django.db import models


class Customer(models.Model):
    """
    Modelo responsável por representar um cliente no sistema.

    Este modelo centraliza os dados cadastrais utilizados
    em pedidos, faturamento e relacionamento com o cliente.
    """

    class Status(models.TextChoices):
        """
        Status do cliente no sistema.

        ACTIVE   → cliente ativo e apto a realizar pedidos
        INACTIVE → cliente desativado (não deve aparecer em fluxos principais)
        """
        ACTIVE = "active", "Ativo"
        INACTIVE = "inactive", "Inativo"

    name = models.CharField("nome", max_length=150)
    email = models.EmailField("e-mail", unique=True)

    # telefone não obrigatório (pode ser preenchido posteriormente)
    phone = models.CharField("telefone", max_length=20, blank=True)

    # pode representar CPF/CNPJ no futuro (validação será adicionada depois)
    document = models.CharField("documento", max_length=20, blank=True)

    status = models.CharField(
        "status",
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE,
    )

    # controle automático de auditoria
    created_at = models.DateTimeField("criado em", auto_now_add=True)
    updated_at = models.DateTimeField("atualizado em", auto_now=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["name"]  # ordenação padrão para listagens

    def __str__(self):
        return self.name