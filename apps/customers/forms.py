from django import forms
from apps.customers.models import Customer


class CustomerForm(forms.ModelForm):
    """
    Formulário para criação e edição de clientes.

    Responsável por validar e normalizar os dados antes de persistir.
    """

    class Meta:
        model = Customer
        fields = ["name", "email", "phone", "document", "status"]

    def clean_name(self):
        """
        Garante que o nome tenha pelo menos 3 caracteres válidos.
        """
        name = self.cleaned_data["name"].strip()

        if len(name) < 3:
            raise forms.ValidationError(
                "O nome deve ter pelo menos 3 caracteres."
            )

        return name