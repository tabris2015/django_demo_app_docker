from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, ListView
from .models import Item, Encargado, Prestamo, Categoria
from .forms import ItemForm, PrestamoItemForm


class CrearYListarView(View):
    name = 'objects'
    template = 'default'
    form = None
    model = None

    def get(self, request):
        return render(
            request,
            self.template,
            {
                self.name: self.model.objects.all(),
                'form': self.form()
            }
        )

    def post(self, request):
        form = self.form(request.POST)
        form.save()
        return HttpResponseRedirect(reverse(f'inventario:{self.name}'))


class ItemView(CrearYListarView):
    name = 'items'
    template = 'inventario/items.html'
    form = ItemForm
    model = Item


class ItemDetailView(DetailView):
    model = Item
    template_name = 'inventario/detalle_item.html'
    slug_field = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        prestamo_form = PrestamoItemForm({'item_id': context['object'].id})
        context['prestamo_form'] = prestamo_form
        return context

    def post(self, request, slug):
        prestamo_form = PrestamoItemForm(request.POST)
        if prestamo_form.is_valid():
            item = Item.objects.get(pk=prestamo_form.cleaned_data['item_id'])
            prestamo = Prestamo(item=item)
            prestamo.save()
            if item.cantidad > 0:
                item.cantidad -= 1
                item.save()

        return HttpResponseRedirect(reverse('inventario:items'))


class EncargadoDetailView(DetailView):
    model = Encargado
    template_name = 'inventario/detalle_encargado.html'
    slug_field = 'id'


class PrestamoListView(ListView):
    model = Prestamo
    context_object_name = 'prestamos'
    template_name = 'inventario/prestamos.html'


class EncargadoListView(ListView):
    model = Encargado
    context_object_name = 'encargados'
    template_name = 'inventario/encargados.html'
