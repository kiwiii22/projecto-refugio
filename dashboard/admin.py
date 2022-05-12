from django.contrib import admin
from .models import Product, Order, Vacuna
from django.contrib.auth.models import Group

admin.site.site_header = 'Refugio de Mascotas'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','especie','sexo','edad','fecha_rescate','image')
    list_filter = ['sexo']

class OrderAdmin(admin.ModelAdmin):
    list_display = ('nombre_de_mascota','edad_solicitante','direccion','telefono','razones_para_adoptar')

class VacunasAdmin(admin.ModelAdmin):
    list_display = ('nombre_de_vacuna'),

# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Vacuna, VacunasAdmin)
#admin.site.unregister(Group)


