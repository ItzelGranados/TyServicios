from posts.models import Requisito
import csv

with open('Matriz/csv/Requisitos.csv', 'r') as file:
    Requisito.objects.all().delete()
    reader = csv.reader(file)
    headers = next(reader)
    i = 2
    for row in reader:
        resolucion = Requisito(nombre_requisito=row[1], nombre=row[4], articulo=row[5], fraccion=row[6])
        resolucion.save()
        print("Listo", i)
        i = i + 1
