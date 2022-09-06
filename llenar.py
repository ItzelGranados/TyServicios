from posts.models import CriterioResolucion
import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TyServicios.settings")
django.setup()

with open('Matriz/csv/CriterioResolucion.csv', 'r') as file:
    CriterioResolucion.objects.all().delete()
    reader = csv.reader(file)
    headers = next(reader)
    i = 2
    for row in reader:
        resolucion = CriterioResolucion(nombre_criterio=row[2], nombre=row[5],
                                        articulo=row[6], fraccion=row[7])
        resolucion.save()
        print("Listo", i)
        i = i + 1
