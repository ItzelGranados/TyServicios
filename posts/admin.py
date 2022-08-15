from django.contrib import admin
from .models import Dato, Requisito, Formato, Paso, Cita, Costo, Tiempo, Vigencia, Solicitante, ResponsableResolucion, \
    FundamentoJuridico, FundamentoJuridico2, FundamentoJuridico3, FundamentoJuridico4, FundamentoJuridico5, FundamentoJuridico6, \
    FundamentoJuridico7, FundamentoJuridico8, Inspeccion, Estadistica, InformacionAdicional

# Register your models here.
admin.site.register(Dato)
admin.site.register(Requisito)
admin.site.register(Formato)
admin.site.register(Paso)
admin.site.register(Cita)
admin.site.register(Costo)
admin.site.register(Tiempo)
admin.site.register(Vigencia)
admin.site.register(Solicitante)
admin.site.register(ResponsableResolucion)
admin.site.register(FundamentoJuridico)
admin.site.register(FundamentoJuridico2)
admin.site.register(FundamentoJuridico3)
admin.site.register(FundamentoJuridico4)
admin.site.register(FundamentoJuridico5)
admin.site.register(FundamentoJuridico6)
admin.site.register(FundamentoJuridico7)
admin.site.register(FundamentoJuridico8)
admin.site.register(Inspeccion)
admin.site.register(Estadistica)
admin.site.register(InformacionAdicional)

