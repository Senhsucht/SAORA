from django.contrib import admin
from SAORA.apps.Inventario.models import *


# Register your models here.

admin.site.register(Producto)
admin.site.register(Inventario)
admin.site.register(Donante)
admin.site.register(Inv_Hist)