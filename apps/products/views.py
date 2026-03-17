from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from apps.products.models import Product
from apps.products.forms import ProductForm


class ProductListView(ListView):
    """
    Exibe a listagem de produtos com paginação e busca simples.
    """
    model = Product
    template_name = "products/product_list.html"
    context_object_name = "products"
    paginate_by = 10  # quantidade de itens por página

    def get_queryset(self):
        """
        Permite busca por nome do produto via query string (?q=...).
        """
        queryset = super().get_queryset()
        search = self.request.GET.get("q", "").strip()

        if search:
            queryset = queryset.filter(name__icontains=search)

        return queryset


class ProductCreateView(CreateView):
    """
    Responsável pela criação de novos produtos.
    """
    model = Product
    form_class = ProductForm
    template_name = "products/product_form.html"
    success_url = reverse_lazy("products:list")  # redireciona após sucesso


class ProductUpdateView(UpdateView):
    """
    Responsável pela edição de produtos existentes.
    """
    model = Product
    form_class = ProductForm
    template_name = "products/product_form.html"
    success_url = reverse_lazy("products:list")


class ProductDeleteView(DeleteView):
    """
    Responsável pela exclusão de produtos com confirmação.
    """
    model = Product
    template_name = "products/product_confirm_delete.html"
    success_url = reverse_lazy("products:list")