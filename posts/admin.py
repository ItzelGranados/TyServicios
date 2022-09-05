from django.contrib import admin
from .models import DatoGeneral, Ambito, FormaPago, Modalidad, NivelDeGobierno, OrdenamientoJuridico, OriginalCopia, Paso, Tipo, \
    TipoTramite, TipoResolucion, TipoSolicitante, Requisito, CriterioResolucion, UbicacionPago, EtapaPago

# Register your models here.
admin.site.register(DatoGeneral)
admin.site.register(Ambito)
admin.site.register(FormaPago)
admin.site.register(Modalidad)
admin.site.register(NivelDeGobierno)
admin.site.register(OrdenamientoJuridico)
admin.site.register(OriginalCopia)
admin.site.register(Paso)
admin.site.register(Tipo)
admin.site.register(Requisito)
admin.site.register(TipoTramite)
admin.site.register(TipoResolucion)
admin.site.register(TipoSolicitante)
admin.site.register(CriterioResolucion)
admin.site.register(UbicacionPago)
admin.site.register(EtapaPago)


