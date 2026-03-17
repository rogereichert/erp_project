from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from apps.customers.models import Customer
from apps.customers.forms import CustomerForm


class CustomerListView(ListView):
    """
    View responsável por exibir a listagem de clientes.

    Suporta:
    - paginação
    - busca por múltiplos campos
    """

    model = Customer
    template_name = "customers/customer_list.html"
    context_object_name = "customers"
    paginate_by = 10  # define quantidade de itens por página

    def get_queryset(self):
        """
        Sobrescreve o queryset padrão para aplicar filtro de busca.

        A busca é feita via query string (?q=valor) e considera:
        - nome
        - email
        - telefone
        - documento
        """
        queryset = super().get_queryset()

        # captura o termo de busca da URL e remove espaços extras
        search = self.request.GET.get("q", "").strip()

        if search:
            # aplica filtro OR entre múltiplos campos
            queryset = queryset.filter(
                Q(name__icontains=search)
                | Q(email__icontains=search)
                | Q(phone__icontains=search)
                | Q(document__icontains=search)
            )

        return queryset

    def get_context_data(self, **kwargs):
        """
        Adiciona o termo de busca ao contexto.

        Isso permite manter o valor no input de busca após submit.
        """
        context = super().get_context_data(**kwargs)

        context["search"] = self.request.GET.get("q", "").strip()

        return context