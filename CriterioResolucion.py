from posts.models import CriterioResolucion, NivelDeGobierno, OrdenamientoJuridico
from functions import no_aplica
import json
import csv

with open("Matriz/norm.json", 'r') as data:
    dictNorm = json.load(data)

with open('Matriz/csv/CriterioResolucion.csv', 'r') as file:
    CriterioResolucion.objects.all().delete()
    reader = csv.reader(file)
    headers = next(reader)
    i = 2
    for row in reader:
        listNivel = ['Federal', 'Estatal', 'Municipal']
        listOrden = ['Constitución', 'Lineamiento', 'Ley', 'Reglamento', 'Manual', 'Código','Acuerdo', 'Norma']
        fed_est = NivelDeGobierno.objects.get(nombre=no_aplica(row[3], listNivel))
        ley_reg = OrdenamientoJuridico.objects.get(nombre=no_aplica(row[4], listOrden))
        resolucion = CriterioResolucion(numero_resolucion=row[0], nombre_criterio=row[2].capitalize(), nivel=fed_est,
                                        ley_reglamento=ley_reg, nombre=row[5],
                                        articulo=row[6], fraccion=row[7])
        print("Listo", i)
        resolucion.save()

        i = i + 1
