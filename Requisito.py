from posts.models import Requisito, NivelDeGobierno, OrdenamientoJuridico
import csv

with open('Matriz/csv/Requisitos.csv', 'r') as file:
    Requisito.objects.all().delete()
    reader = csv.reader(file)
    headers = next(reader)
    i = 2
    for row in reader:
        fed_est = NivelDeGobierno.objects.get(nombre=row[2])
        ley_reg = OrdenamientoJuridico.objects.get(nombre=row[3])
        resolucion = Requisito(numero_requisito=row[0], nombre_requisito=row[1], federal_estatal=fed_est,
                               ley_reglamento=ley_reg, nombre=row[4], articulo=row[5], fraccion=row[6])
        resolucion.save()
        print("Listo", i)
        i = i + 1
