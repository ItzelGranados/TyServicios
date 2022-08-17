from django.utils import timezone
from django.views.generic import DetailView
from django.views.generic import TemplateView
from posts.models import DatoGeneral, Ambito, FormaPago, Modalidad, NivelDeGobierno, OrdenamientoJuridico, OriginalCopia, Paso, Tipo, \
    TipoTramite, TipoResolucion, TipoSolicitante, Requisito


class HomeView(TemplateView):
    template_name = "index.html"

    #model = Ambito

    """def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()"""

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
