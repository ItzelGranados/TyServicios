from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from posts.models import DatoGeneral, Ambito, FormaPago, Modalidad, NivelDeGobierno, OrdenamientoJuridico, OriginalCopia, Paso, Tipo, \
    TipoTramite, TipoResolucion, TipoSolicitante, Requisito


class DatoGeneralListViews(ListView):
    model = Ambito
    context_object_name = "notes"
    template_name = "notes/index.html"

class DatoGeneralDetalView(DetailView):
    models = Ambito
    context_object_name = "note"



    """dato = DatoGeneral.objects.all()
    forma = FormaPago.objects.all()
    modalidad = Modalidad.objects.all()
    nivel_gobierno = NivelDeGobierno.objects.all()
    ordenamiento = OrdenamientoJuridico.objects.all()
    original_copia = OriginalCopia.objects.all()
    pasos = Paso.objects.all()
    tipo = Tipo.all()
    requisito = Requisito.all()
    tipo_tramite = TipoTramite.all()
    tipo_resolucion = TipoResolucion.all()
    tipo_solicitante = TipoSolicitante.all()"""



# Create your views here.
