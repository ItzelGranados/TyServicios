from posts.models import CriterioResolucion, NivelDeGobierno, OrdenamientoJuridico
import csv

with open('Matriz/csv/CriterioResolucion.csv', 'r') as file:
    CriterioResolucion.objects.all().delete()
    reader = csv.reader(file)
    headers = next(reader)
    i = 2
    for row in reader:
        # 3 y 4
        fed_est = NivelDeGobierno.objects.get(nombre=row[3])
        ley_reg = OrdenamientoJuridico.objects.get(nombre=row[4])
        resolucion = CriterioResolucion(nombre_criterio=row[2], nivel=fed_est, ley_reglamento=ley_reg, nombre=row[5],
                                        articulo=row[6], fraccion=row[7])
        print("Listo", i)
        resolucion.save()

        i = i + 1
