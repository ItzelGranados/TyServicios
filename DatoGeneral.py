from posts.models import DatoGeneral, Tipo, TipoTramite, NivelDeGobierno, Ambito, OrdenamientoJuridico, OriginalCopia, \
    Paso, TipoResolucion, TipoSolicitante, Requisito, CriterioResolucion, Modalidad, UbicacionPago, FormaPago, EtapaPago
from functions import no_aplica
import json
import csv

with open("Matriz/norm.json", 'r') as data:
    dictNorm = json.load(data)

with open('Matriz/csv/DatoGeneral.csv', 'r') as file:
    DatoGeneral.objects.all().delete()
    reader = csv.reader(file)
    headers = next(reader)
    i = 2
    for row in reader:
        tipoTram = Tipo.objects.get(nombre=no_aplica(row[3], dictNorm["Tipos"]))
        ley_reg = TipoTramite.objects.get(nombre=no_aplica(row[4], dictNorm["Tramites"]))

        niv_gob = NivelDeGobierno.objects.get(nombre=no_aplica(row[7], dictNorm["NivelGobierno"]))

        Amb_fun = Ambito.objects.get(nombre=no_aplica(row[9], dictNorm["Ambitos"]))
        Tip_fun = OrdenamientoJuridico.objects.get(nombre=no_aplica(row[10], dictNorm["Ordenamiento"]))

        Ori_cop = OriginalCopia.objects.get(nombre=no_aplica(row[16], dictNorm["OriginalCopia"]))
        Amb_req = NivelDeGobierno.objects.get(nombre=no_aplica(row[25], dictNorm["NivelGobierno"]))
        Tip_req = OrdenamientoJuridico.objects.get(nombre=no_aplica(row[26], dictNorm["Ordenamiento"]))

        Amb_fun_med = NivelDeGobierno.objects.get(nombre=no_aplica(row[33], dictNorm["NivelGobierno"]))
        Tip_fun_med = OrdenamientoJuridico.objects.get(nombre=no_aplica(row[34], dictNorm["Ordenamiento"]))

        Pasos = Paso.objects.get(nombre=no_aplica(row[38], dictNorm["Pasos"]))
        Amb_fun_der = Ambito.objects.get(nombre=no_aplica(row[50], dictNorm["Ambitos"]))
        Tip_fun_der = OrdenamientoJuridico.objects.get(nombre=no_aplica(row[51], dictNorm["Ordenamiento"]))

        A_fun_der = Ambito.objects.get(nombre=no_aplica(row[59], dictNorm["Ambitos"]))
        T_fun_pla = OrdenamientoJuridico.objects.get(nombre=no_aplica(row[60], dictNorm["Ordenamiento"]))

        Amb_fun_fic = Ambito.objects.get(nombre=no_aplica(row[64], dictNorm["Ambitos"]))
        Tip_fun_fic = OrdenamientoJuridico.objects.get(nombre=no_aplica(row[65], dictNorm["Ordenamiento"]))

        Tip_res = TipoResolucion.objects.get(nombre=no_aplica(row[75], dictNorm["Resoluciones"]))
        Per_sol = TipoSolicitante.objects.get(nombre=no_aplica(row[92], dictNorm["Solicitantes"]))
        Amb_ins = Ambito.objects.get(nombre=no_aplica(row[116], dictNorm["Ambitos"]))

        Tip_ins = Tipo.objects.get(nombre=no_aplica(row[117], dictNorm["Tipos"]))
        Amb_inf = Ambito.objects.get(nombre=no_aplica(row[122], dictNorm["Ambitos"]))
        Tip_inf = OrdenamientoJuridico.objects.get(nombre=no_aplica(row[123], dictNorm["Ordenamiento"]))

        # Requisito.objects.get(numero_requisito=row[15])

        # Many to Many 15, 32,
        resolucion = DatoGeneral.objects.create(homoclave_anterior=row[0], homoclave=row[1], nombre_tramite=row[2],
                                                tipo=tipoTram,
                                                tipo_tramite=ley_reg, depedencia=row[5], unidad_administrativa=row[6],
                                                nivel_gobierno=niv_gob, descripcion_principal=row[8],
                                                ambito_fundamento_origen=Amb_fun
                                                , tipo_fundamento_origen=Tip_fun, nombre_fundamento_origen=row[11],
                                                articulo_fundamento_origen=row[12], fraccion_fundamento_origen=row[13],
                                                numero_requisitos=row[14], original_copia=Ori_cop, descripcion=row[17],
                                                formato=row[18], naturaleza=row[19], tiempo_promedio=row[20],
                                                firma_validacion=row[21],
                                                persona_emite=row[22], requisito_solicitado=row[23],
                                                nombre_dependencia=row[24],
                                                ambito_requisito=Amb_req, tipo_requisito=Tip_req,
                                                nombre_fundamento_requisito=row[27],
                                                articulo_fundamento_requisito=row[28],
                                                fraccion_fundamento_requisito=row[29],
                                                nombre_formato=row[30], numero_identificador=row[31],
                                                ambito_fundamento_medio=Amb_fun_med, tipo_fundamento_medio=Tip_fun_med,
                                                nombre_fundamento_medio=row[35], articulo_fundamento_medio=row[36],
                                                fraccion_fundamento_medio=row[37], pasos=Pasos,
                                                puede_agendar_cita=row[39], puede_realizar_tramite=row[40],
                                                medio_cita=row[41],
                                                monto=row[42], moneda_pago=row[43], metodologia_monto=row[44],
                                                vigencia_pago=row[48],
                                                fundamento_monto_derechos=row[49],
                                                ambito_fundamento_derechos=Amb_fun_der,
                                                tipo_fundamento_derechos=Tip_fun_der, nombre_fundamento_derecho=row[52],
                                                articulo_fundamento_derechos=row[53],
                                                fraccion_fundamento_derechos=row[54],
                                                tiempo_resolucion=row[55], plazo_prevenir=row[56],
                                                plazo_responder=row[57],
                                                derecho_respuesta=row[58], a_fundamento_plazo_maximo=A_fun_der,
                                                t_fundamento_plazo_maximo=T_fun_pla, n_fundamento_plazo_maximo=row[61],
                                                ar_fundamento_plazo_maximo=row[62],
                                                frac_fundamento_plazo_maximo=row[63],
                                                ambito_fundamento_ficta=Amb_fun_fic, tipo_fundamento_ficta=Tip_fun_fic,
                                                nombre_fundamento_ficta=row[66], articulo_fundamento_ficta=row[67],
                                                fraccion_fundamento_ficta=row[68], fundamento_prevencion=row[69],
                                                ambito_fundamento_prevencion=row[70],
                                                tipo_fundamento_prevencion=row[71],
                                                nombre_fundamento_prevencion=row[72],
                                                articulo_fundamento_prevencion=row[73],
                                                fraccion_fundamento_prevencion=row[74], tipo_resolucion=Tip_res,
                                                vigencia=row[82],
                                                ambito_fundamento_vigencia=row[83], tipo_fundamento_vigencia=row[84],
                                                nombre_fundamento_vigencia=row[85],
                                                articulo_fundamento_vigencia=row[86],
                                                fraccion_fundamento_vigencia=row[87], resolucion=row[88],
                                                liga_tramite=row[89],
                                                resolucion_requisito=row[90], liga_resolucion=row[91],
                                                persona_solicitante=Per_sol,
                                                funcionalidad_tramite=row[93], caso_solicitud=row[94],
                                                actividad_economica=row[95],
                                                detalle=row[96], subsector=row[97], rama=row[98], subrama=row[99],
                                                clase=row[100],
                                                responsable_tramite=row[101], nombre=row[102], rol_funcionario=row[103],
                                                cargo=row[104], correo_electronico=row[105], otro=row[106],
                                                telefono=row[107],
                                                extension=row[108], datos_responsable=row[109], organo=row[110],
                                                quejas_denuncias=row[111], inspeccion=row[112], objetivo=row[113],
                                                liga_acceso=row[114], conservar_informacion=row[115],
                                                ambito_inspeccion_verificacion=Amb_ins,
                                                tipo_inspeccion_verificacion=Tip_ins,
                                                nombre_inspeccion_verificacion=row[118], articulo_vigencia=row[119],
                                                fraccion_inspeccion_verificacion=row[120],
                                                fundamento_informacion=row[121],
                                                ambito_informacion=Amb_inf, tipo_informacion=Tip_inf,
                                                nombre_informacion=row[124], articulo_informacion=row[125],
                                                fraccion_informacion=row[126], registro_regulaciones_canal=row[127],
                                                solicitudes_recibidas=row[128], total_solicitudes_recibidas=row[129],
                                                informacion=row[130], informacion_interesado=row[131],
                                                protesta_ciudadana=row[132],
                                                cantidad_protestas=row[133], momento_vida=row[134])

        # Separación de la lista de números lo separa por las ',' y después se convierte de string a int
        # y si la entrada es 'No aplica' se retorna el número de requisito 0
        listaDeRequisitos = list(map(int, row[15].split(','))) if (row[15] != 'No aplica') else [0]

        # Se busca el número del requisito que se encuentra en cada elemento de la lista de números de requisitos
        numRequisito = [Requisito.objects.get(numero_requisito=requisito) for requisito in listaDeRequisitos]

        resolucion.requisitos.add(*numRequisito)

        listaDeModalidad = list(row[32].split(',')) if (row[32] != 'No aplica') else [0]
        tipModalidad = [Modalidad.objects.get(nombre=modalidad) for modalidad in
                        listaDeModalidad]

        resolucion.modalidades.add(*tipModalidad)

        listaDeUbic = list(row[45].split(',')) if (row[45] != 'No Aplica') else ['No aplica']
        ubicacionPag = [UbicacionPago.objects.get(nombre=ubicacion) for ubicacion in
                        listaDeUbic]

        resolucion.realizar_pago.add(*ubicacionPag)

        listaDePago = list(row[46].split(',')) if (row[46] != 'No Aplica') else ['No aplica']
        tipPago = [FormaPago.objects.get(nombre=pago) for pago in
                   listaDePago]

        resolucion.forma_pago.add(*tipPago)

        listaDeEtapa = list(row[47].split(',')) if (row[47] != 'No Aplica') else ['No aplica']
        tipEtaoa = [EtapaPago.objects.get(nombre=etapa) for etapa in
                    listaDeEtapa]

        resolucion.etapa_tramite.add(*tipEtaoa)

        listaDeResolucion = list(map(int, row[76].split(','))) if (row[76] != 'No aplica') else [0]
        numResolucion = [CriterioResolucion.objects.get(numero_resolucion=resolucion) for resolucion in
                         listaDeResolucion]

        resolucion.fundamento_resolucion.add(*numResolucion)

        print("Listo", i)
        i = i + 1
