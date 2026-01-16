from django.contrib import admin

from .models import Categoria, Gasto, PresupuestoCategoria, ConfiguracionUsuario

# Register your models here.

admin.site.register(ConfiguracionUsuario)
admin.site.register(Categoria)
admin.site.register(Gasto)
admin.site.register(PresupuestoCategoria)