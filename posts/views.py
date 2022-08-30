from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from posts.models import DatoGeneral


class DatoGeneralListViews(ListView):
    model = DatoGeneral
    template_name = "lista_tramites.html"


class DatoGeneralDetailView(DetailView):
    models = DatoGeneral
    queryset = DatoGeneral.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        # context['dato_list'] = DatoGeneral.objects.all()
        return context

    template_name = "detalle_tramite.html"