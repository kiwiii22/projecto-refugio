from pyexpat import model
from attr import field
from django import forms
from matplotlib.pyplot import cla
from .models import Order, Product, Vacuna

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['id','nombre','especie','sexo', 'edad','fecha_rescate','image']

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['nombre_de_mascota','edad_solicitante','direccion','telefono','razones_para_adoptar']

class VacunaForm(forms.ModelForm):
    class Meta:
        model = Vacuna
        fields = ['nombre_de_vacuna']


