from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required, permission_required
from .views import ItemView, ItemDetailView, EncargadoDetailView, PrestamoListView, EncargadoListView


app_name = 'inventario'
urlpatterns = [
    path(
        '',
        TemplateView.as_view(template_name='inventario/index.html'),
        name='index'
    ),
    path(
        'items/',
        ItemView.as_view(),
        name='items'
    ),
    path(
        'items/detalle/<slug:slug>/',
        ItemDetailView.as_view(),
        name='detalle_item'
    ),
    path(
        'encargados/',
        EncargadoListView.as_view(),
        name='encargados'
    ),
    path(
        'encargados/detalle/<slug:slug>/',
        EncargadoDetailView.as_view(),
        name='detalle_encargado'
    ),
    path(
        'prestamos/',
        PrestamoListView.as_view(),
        name='prestamos'
    ),
]
