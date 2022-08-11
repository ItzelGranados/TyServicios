from django.shortcuts import render, HttpResponse

from django.views.generic import TemplateView
from posts.models import Dato, Requisito, Formato, Paso, Cita, Costo, Tiempo, Vigencia, Solicitante, ResponsableResolucion, \
    FundamentoJuridico, FundamentoJuridico2, FundamentoJuridico3, FundamentoJuridico4, FundamentoJuridico5, FundamentoJuridico6, \
    FundamentoJuridico7, FundamentoJuridico8, Inspeccion, Estadistica, InformacionAdicional


class HomeView(TemplateView):
    d = Dato.objects.all()
    r = Requisito.objects.all()
    f = Formato.objects.all()
    p = Paso.objects.all()
    c = Cita.objects.all()
    co = Costo.objects.all()
    t = Tiempo.objects.all()
    v = Vigencia.objects.all()
    s = Solicitante.objects.all()
    re = ResponsableResolucion.all()
    fun = FundamentoJuridico.all()
    f2 = FundamentoJuridico2.all()
    f3 = FundamentoJuridico3.all()
    f4 = FundamentoJuridico4.all()
    f5 = FundamentoJuridico5.all()
    f6 = FundamentoJuridico6.all()
    f7 = FundamentoJuridico7.all()
    f8 = FundamentoJuridico8.all()
    i = Inspeccion.all()
    e = Estadistica.all()
    info = InformacionAdicional.all()

    template_name = "index.html"

# Create your views here.
