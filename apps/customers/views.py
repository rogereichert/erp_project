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

class CustomerCreateView(CreateView):
    """
    View responsável pela criação de novos clientes.
    """

    model = Customer
    form_class = CustomerForm
    template_name = "customers/customer_form.html"
    success_url = reverse_lazy("customers:list")

    def form_valid(self, form):
        """
        Exibe mensagem de sucesso após criação.
        """
        from django.contrib import messages

        response = super().form_valid(form)
        messages.success(self.request, "Cliente criado com sucesso.")
        return response

    def get_context_data(self, **kwargs):
        """
        Adiciona título para uso no template.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Novo Cliente"
        return context


class CustomerUpdateView(UpdateView):
    """
    View responsável pela edição de clientes existentes.

    Reutiliza o mesmo formulário e template da criação,
    garantindo consistência na interface.
    """
    model = Customer
    form_class = CustomerForm
    template_name = "customers/customer_form.html"
    success_url = reverse_lazy("customers:list")  # redirecionamento após atualização


class CustomerDeleteView(DeleteView):
    """
    View responsável pela exclusão de clientes.

    Exibe uma tela de confirmação antes de remover o registro.
    """
    model = Customer
    template_name = "customers/customer_confirm_delete.html"
    success_url = reverse_lazy("customers:list")  # redirecionamento após exclusão