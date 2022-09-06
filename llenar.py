import csv

import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TyServicios.settings")  # project_name nombre del proyecto
django.setup()

from posts.models import CriterioResolucion

with open('Matriz/csv/CriterioResolucion.csv', 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)
    i = 2
    for row in reader:
        resolucion = CriterioResolucion(nombre_criterio=row[2], nombre=row[5],
                                        articulo=row[6], fraccion=row[7])
        try:
            resolucion.save()
            print("Save", i)
        except:
            #resolucion.save()
            print("Listo", i)
            i = i+1
'''
        try:
            #resolucion.save()
        except:
            print("error")

'''