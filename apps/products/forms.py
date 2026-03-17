from decimal import Decimal
from django import forms
from apps.products.models import Product


class ProductForm(forms.ModelForm):
    """
    Formulário para criação e edição de produtos.

    Responsável por validar dados comerciais e garantir consistência
    antes de persistir no banco.
    """

    class Meta:
        model = Product
        fields = ["sku", "name", "description", "price", "status"]

    def clean_sku(self):
        """
        Normaliza o SKU para padrão consistente (caixa alta e sem espaços).
        Também valida duplicidade com mensagem amigável.
        """
        sku = self.cleaned_data["sku"].strip().upper()

        if Product.objects.filter(sku=sku).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Já existe um produto com este SKU.")

        return sku

    def clean_price(self):
        """
        Garante que o preço seja maior que zero.
        """
        price = self.cleaned_data["price"]

        if price <= Decimal("0.00"):
            raise forms.ValidationError("O preço deve ser maior que zero.")

        return price