# apps/core/urls.py
from django.urls import path
from apps.core.views import DashboardView

# namespace da aplicação core
app_name = "core"

urlpatterns = [
    # rota principal do sistema (dashboard)
    path("", DashboardView.as_view(), name="dashboard"),
]