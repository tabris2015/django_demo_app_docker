from django import forms
from .models import Item, Categoria, Encargado, Prestamo


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']


class EncargadoForm(forms.ModelForm):
    class Meta:
        model = Encargado
        fields = ['nombre', 'carrera']


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['nombre', 'marca', 'categoria', 'encargado', 'cantidad']


class PrestamoItemForm(forms.Form):
    item_id = forms.IntegerField(widget=forms.HiddenInput())
