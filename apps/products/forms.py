from django import forms
from decimal import Decimal
from apps.products.models import Product


class ProductForm(forms.ModelForm):
    """
    Formulário para criação e edição de produtos.

    Responsável por validar dados comerciais antes de persistir.
    """

    class Meta:
        model = Product
        fields = ["sku", "name", "description", "price", "status"]

    def clean_sku(self):
        sku = self.cleaned_data["sku"].strip().upper()
        return sku

    def clean_price(self):
        """
        Garante que o preço seja maior que zero.
        """
        price = self.cleaned_data["price"]

        if price <= Decimal("0.00"):
            raise forms.ValidationError("O preço deve ser maior que zero.")

        return price