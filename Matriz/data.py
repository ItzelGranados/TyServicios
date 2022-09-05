from csv import DictReader
from datetime import datetime


from django.core.management import BaseCommand

from posts.models import DatoGeneral, Ambito, FormaPago, Modalidad, NivelDeGobierno, OrdenamientoJuridico, OriginalCopia, Paso, Tipo, \
    TipoTramite, TipoResolucion, TipoSolicitante, Requisito



DATETIME_FORMAT = '%m/%d/%Y %H:%M'

NAMES = [
    'DatoGeneral'
    'Ambito'
    'FormaPago'
    'Modalidad'
    'NivelDeGobierno'
    'OrdenamientoJuridico'
    'OriginalCopia'
    'Paso'
    'Tipo'
    'TipoTramite'
    'TipoResolucion'
    'TipoSolicitante'
    'Requisito'

]


class Command(BaseCommand):
    #Show this when the user types help

    help = "Loads data from matrizTyServicios.csv into our Pet mode"

    def handle(self, *args, **options):
       for row in DictReader(open('matrizTyServicios.xlsx')):
           dato_general = DatoGeneral()
           dato_general.homoclave = row['Homoclave']

