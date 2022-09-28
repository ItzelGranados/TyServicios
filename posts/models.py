from django.db import models


class Ambito(models.Model):
    nombre = models.CharField(max_length=25)

    def __str__(self):
        return self.nombre


class FormaPago(models.Model):
    nombre = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre


class Modalidad(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class NivelDeGobierno(models.Model):
    nombre = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre


class OrdenamientoJuridico(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class OriginalCopia(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Paso(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Tipo(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Tipo", null=True, blank=True)

    def __str__(self):
        return self.nombre


class TipoTramite(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class TipoResolucion(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class TipoSolicitante(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre



class UbicacionPago(models.Model):
    nombre = models.CharField(max_length=250, null=True, blank=True, verbose_name="¿En dónde puede realizar el pago?")

    def __str__(self):
        return self.nombre

class EtapaPago(models.Model):
    nombre = models.CharField(max_length=200, null=True, blank=True, verbose_name=" Etapa del pago")

    def __str__(self):
        return self.nombre

class CriterioResolucion(models.Model):

    numero_resolucion = models.IntegerField(null=True, blank=True, verbose_name="Numero de resolución")
    nombre_criterio = models.CharField(max_length=250, null=True, blank=True, verbose_name="Nombre criterio")
    nivel = models.ForeignKey(NivelDeGobierno, on_delete=models.PROTECT, null=True, blank=True, related_name="+")
    ley_reglamento = models.ForeignKey(OrdenamientoJuridico, on_delete=models.PROTECT, null=True, blank=True, related_name="+")
    nombre = models.CharField(max_length=250, null=True, blank=True, verbose_name="Nombre")
    articulo = models.CharField(max_length=250, null=True, blank=True, verbose_name="Artículo")
    fraccion = models.CharField(max_length=250, null=True, blank=True, verbose_name="Fracción y/o inciso")
    def __str__(self):
        return self.nombre


class Requisito(models.Model):
    nombre_requisito = models.TextField(max_length=500, null=True, blank=True, verbose_name="Nombre del requisito")
    numero_requisito = models.IntegerField(null=True, blank=True, verbose_name="Numero de requisito")
    federal_estatal = models.ForeignKey(NivelDeGobierno, on_delete=models.PROTECT, null=True, blank=True, related_name="+")
    ley_reglamento = models.ForeignKey(OrdenamientoJuridico, on_delete=models.PROTECT, null=True, blank=True, related_name="+")
    nombre = models.CharField(max_length=255, null=True, blank=True, verbose_name="Nombre")
    articulo = models.CharField(max_length=100, null=True, blank=True, verbose_name="Artículo")
    fraccion = models.CharField(max_length=100, null=True, blank=True, verbose_name="Fracción y/o Inciso")


    def __str__(self):
        return self.nombre


class DatoGeneral(models.Model):

    homoclave_anterior = models.CharField(max_length=40, blank=True, null=True, verbose_name="Homoclave anterior")
    homoclave = models.CharField(max_length=40, blank=True, null=True, verbose_name="Homoclave")
    nombre_tramite = models.CharField(max_length=150, null=True, blank=True, verbose_name="Nombre del trámite")
    tipo = models.ForeignKey(Tipo, null=True, blank=True, on_delete=models.PROTECT, verbose_name= "Tipo de Servicio o Tramite")
    tipo_tramite = models.ForeignKey(TipoTramite, null=True, blank=True, on_delete=models.PROTECT, verbose_name="Tipo de trámite")
    depedencia = models.CharField(max_length=200, null=True, verbose_name="Depedencia")
    unidad_administrativa = models.CharField(max_length=250, null=True, blank=True, verbose_name="Unidad Administrativa")
    nivel_gobierno = models.ForeignKey(NivelDeGobierno, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Nivel de gobierno")
    descripcion_principal = models.TextField(max_length=500, blank=True, null=True, verbose_name="Descripción")

    ambito_fundamento_origen = models.ForeignKey(Ambito, on_delete=models.PROTECT, blank=True, null=True, related_name="Ámbito")
    tipo_fundamento_origen = models.ForeignKey(OrdenamientoJuridico, on_delete=models.PROTECT,blank=True, null=True, verbose_name="Tipo")
    nombre_fundamento_origen = models.CharField(max_length=250, blank=True, null=True, verbose_name="Nombre")
    articulo_fundamento_origen = models.CharField(max_length=250, blank=True, null=True, verbose_name="Artículo")
    fraccion_fundamento_origen = models.CharField(max_length=250,blank=True, null=True, verbose_name="Fracción")

    numero_requisitos = models.IntegerField(blank=True, null=True, verbose_name="Requisitos")
    requisitos = models.ManyToManyField(Requisito, blank=True, verbose_name="Nombre del requisito")

    original_copia = models.ForeignKey(OriginalCopia, on_delete=models.PROTECT, null=True, blank=True,
                                       verbose_name="Original o copia")

    descripcion = models.CharField(max_length=200, null=True, blank=True, verbose_name="Descripción")

    formato = models.BooleanField(default=False, null=True, blank=True, verbose_name="¿Forma parte del formato?")

    naturaleza = models.TextField(null=True, blank=True, verbose_name="Naturaleza")
    tiempo_promedio = models.IntegerField(null=True, blank=True,
                                          verbose_name="Tiempo promedio en conseguir el requisito para su presentación (horas)")
    firma_validacion = models.BooleanField(default=False, null=True, blank=True,
                                           verbose_name="¿Es necesario alguna firma, validación, certificación, autorización o visto bueno de un tercero?")
    persona_emite = models.CharField(max_length=200, null=True, blank=True,
                                     verbose_name="Nombre de la empresa o persona que lo emite")
    requisito_solicitado = models.BooleanField(default=False, null=True, blank=True,
                                               verbose_name="¿El requisito solicitado es un trámite que se debe realizar con alguna dependencia gubernamental?")
    nombre_dependencia = models.CharField(max_length=100, null=True, blank=True,
                                          verbose_name="Nombre de la dependencia, ubicación y medios de contacto")

    ambito_requisito = models.ForeignKey(NivelDeGobierno, on_delete=models.PROTECT, blank=True, null=True,
                                         related_name="Ámbito")
    tipo_requisito = models.ForeignKey(OrdenamientoJuridico, on_delete=models.PROTECT, blank=True, null=True,
                                       related_name="+")
    nombre_fundamento_requisito = models.CharField(max_length=250, blank=True, null=True, verbose_name="Nombre")
    articulo_fundamento_requisito = models.CharField(max_length=50, blank=True, null=True, verbose_name="Artículo")
    fraccion_fundamento_requisito = models.CharField(max_length=50, blank=True, null=True, verbose_name="Fracción")

    nombre_formato = models.CharField(max_length=250, blank=True, null=True, verbose_name="Nombre del formato")
    numero_identificador = models.CharField(max_length=100, blank=True, null=True, verbose_name ="Número de identificador del formato")
    modalidades = models.ManyToManyField(Modalidad, blank=True, related_name="Modalidad")

    ambito_fundamento_medio = models.ForeignKey(NivelDeGobierno, on_delete=models.PROTECT, blank=True, null=True, related_name="+")
    tipo_fundamento_medio = models.ForeignKey(OrdenamientoJuridico,on_delete=models.PROTECT, blank=True, null=True, related_name="+")
    nombre_fundamento_medio = models.CharField(max_length=250, blank=True, null=True, verbose_name="Nombre")
    articulo_fundamento_medio = models.CharField(max_length=50, blank=True, null=True, verbose_name="Artículo")
    fraccion_fundamento_medio = models.CharField(max_length=20,blank=True, null=True, verbose_name="Fracción y/o inciso")

    pasos = models.ForeignKey(Paso, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Pasos")

    puede_agendar_cita = models.BooleanField(default=False, verbose_name="¿Es obligatorio agendar una cita?")
    puede_realizar_tramite = models.BooleanField(default=False,
                                                 verbose_name="¿Se puede agendar una cita para realizar un trámite?")
    medio_cita = models.URLField(max_length=250, blank=True, null=True, verbose_name="Medio para solicitar la cita")

    monto = models.CharField(max_length=100, null=True, blank=True, verbose_name="Monto")
    moneda_pago = models.CharField(max_length=20,null=True, blank=True, verbose_name="Moneda en la que se realiza el pago")
    metodologia_monto = models.TextField(null=True, blank=True, verbose_name="Metodología utilizada para cálculo del monto")
    realizar_pago = models.ManyToManyField(UbicacionPago,blank=True,
                                     verbose_name="¿En dónde puedo realizar el pago?")
    forma_pago = models.ManyToManyField(FormaPago,blank=True,
                                  verbose_name="Forma de pago")
    etapa_tramite = models.ManyToManyField(EtapaPago,blank=True,
                                     verbose_name="Etapa del trámite o servicio en que se realiza o se puede realizar el pago")

    vigencia_pago = models.CharField(max_length=100, null=True, blank=True,
                                     verbose_name="Vigencia de la línea de captura para realizar el pago en caso de requerirla")

    fundamento_monto_derechos = models.TextField(blank=True, null=True, verbose_name="Fundamento del monto de derechos")
    ambito_fundamento_derechos = models.ForeignKey(Ambito, on_delete=models.PROTECT, blank=True, null=True, related_name="+")
    tipo_fundamento_derechos = models.ForeignKey(OrdenamientoJuridico, on_delete=models.PROTECT, blank=True, null=True, related_name="+")
    nombre_fundamento_derecho = models.CharField(max_length=250, blank=True, null=True, verbose_name="Nombre")
    articulo_fundamento_derechos = models.CharField(max_length=20, blank=True, null = True, verbose_name="Artículo")
    fraccion_fundamento_derechos = models.CharField(max_length=10, blank=True, null=True, verbose_name="Fracción")

    tiempo_resolucion = models.CharField(max_length=50, null=True, blank=True,
                                            verbose_name="Tiempo que tiene la dependencia para resolver")

    plazo_prevenir = models.CharField(max_length=100, null=True, blank=True,
                                      verbose_name="Plazo que tiene la dependencia para prevenir")
    plazo_responder = models.CharField(max_length=50, null=True, blank=True,
                                          verbose_name="Plazo que tiene el usuario para responder la prevención")
    derecho_respuesta = models.CharField(max_length=30, null=True, blank=True,
                                         verbose_name="Derecho del usuario ante la falta de respuesta")

    a_fundamento_plazo_maximo = models.ForeignKey(Ambito, on_delete=models.PROTECT, null=True, blank=True, related_name="+")
    t_fundamento_plazo_maximo = models.ForeignKey(OrdenamientoJuridico, on_delete=models.PROTECT, null=True, blank=True, related_name="Tipo")
    n_fundamento_plazo_maximo = models.CharField(max_length=250, blank=True, null=True, verbose_name="Nombre")
    ar_fundamento_plazo_maximo = models.CharField(max_length=250, null=True, blank=True, verbose_name="Artículo")
    frac_fundamento_plazo_maximo = models.CharField(max_length=250, null=True, blank=True, verbose_name="Fracción")

    ambito_fundamento_ficta = models.ForeignKey(Ambito, on_delete=models.PROTECT, null=True, blank=True, related_name="+")
    tipo_fundamento_ficta = models.ForeignKey(OrdenamientoJuridico, on_delete=models.PROTECT, null=True, blank=True, related_name="+")
    nombre_fundamento_ficta = models.CharField(max_length=100, blank=True, null=True, verbose_name="Nombre")
    articulo_fundamento_ficta = models.CharField(max_length=100, blank=True, null=True, verbose_name="Artículo")
    fraccion_fundamento_ficta = models.CharField(max_length=100, blank=True, null=True, verbose_name="Fracción")

    fundamento_prevencion = models.CharField(max_length=100, blank=True, null=True,verbose_name="Fundamento de la prevención")
    ambito_fundamento_prevencion = models.CharField(max_length=100, blank=True, null=True, verbose_name="Ámbito")
    tipo_fundamento_prevencion = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tipo")
    nombre_fundamento_prevencion = models.CharField(max_length=100, blank=True, null=True, verbose_name="Nombre")
    articulo_fundamento_prevencion = models.CharField(max_length=100, blank=True, null=True, verbose_name="Artículo")
    fraccion_fundamento_prevencion = models.CharField(max_length=100, blank=True, null=True, verbose_name="Fracción")

    tipo_resolucion = models.ForeignKey(TipoResolucion, on_delete=models.PROTECT, null=True, blank=True, related_name="+")
    fundamento_resolucion = models.ManyToManyField(CriterioResolucion, blank=True,
                                             verbose_name="Fundamento del criterio de resolución")


    vigencia = models.CharField(max_length=100, blank=True, null=True, verbose_name="Vigencia")

    ambito_fundamento_vigencia = models.CharField(max_length=100, blank=True, null=True, verbose_name="Ámbito")
    tipo_fundamento_vigencia = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tipo")
    nombre_fundamento_vigencia =models.CharField(max_length=100, blank=True, null=True, verbose_name="Nombre")
    articulo_fundamento_vigencia = models.CharField(max_length=100, blank=True, null=True, verbose_name="Artículo")
    fraccion_fundamento_vigencia = models.CharField(max_length=100, blank=True, null=True, verbose_name="Fracción")

    resolucion = models.BooleanField(default=False, null=True, blank=True,
                                  verbose_name="La resolución de este trámite está vinculada con la presentación de otros trámites")
    liga_tramite = models.CharField(max_length=200, null=True, blank=True,
                                    verbose_name="Liga del trámite con que está vincualdo")

    resolucion_requisito = models.BooleanField(default=False, verbose_name="¿La resolución es requisito de otro trámite?")
    liga_resolución = models.CharField(max_length=200, blank=True, null=True, verbose_name="Liga de la resolución del trámite")

    persona_solicitante = models.ForeignKey(TipoSolicitante,on_delete=models.PROTECT, null=True, blank=True, verbose_name="¿Quién puede solicitarlo?")
    funcionalidad_tramite = models.TextField(max_length=400, null=True, blank=True,
                                             verbose_name="¿Para qué sirve realizar este trámite?")
    caso_solicitud = models.TextField(max_length=500, null=True, blank=True,
                                      verbose_name="¿En qué caso se debe solicitar el trámite o servicio?")
    actividad_economica = models.TextField(max_length=300, null=True, blank=True,
                                           verbose_name="Actividad económica que está vinculada al trámite o servicio")
    detalle = models.TextField(max_length=500, null=True, blank=True, verbose_name="Detalle")
    subsector = models.TextField(max_length=350, null=True, blank=True, verbose_name="Subsector")
    rama = models.TextField(max_length=300, null=True, blank=True, verbose_name="Rama")
    subrama = models.CharField(max_length=150, null=True, blank=True, verbose_name="Subrama")
    clase = models.CharField(max_length=200, null=True, blank=True, verbose_name="Clase")

    responsable_tramite = models.CharField(max_length=100, null=True, blank=True,
                                           verbose_name="Responsable del trámite o servicio")


    nombre = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nombre")
    rol_funcionario = models.CharField(max_length=100, null=True, blank=True, verbose_name="Rol del funcionario")
    cargo = models.CharField(max_length=200, null=True, blank=True, verbose_name="Cargo")
    correo_electronico = models.EmailField(max_length=100, null=True, blank=True, verbose_name="Correo electrónico")
    otro = models.CharField(max_length=30, null=True, blank=True, verbose_name="Otro")
    telefono = models.CharField(max_length=15, null=True, blank=True, verbose_name="Teléfono")
    extension = models.IntegerField(null=True, blank=True, verbose_name="Extensión")
    datos_responsable = models.CharField(null=True, blank=True, max_length=200,
                                         verbose_name="Datos de la oficina del responsable del trámite")
    organo = models.CharField(max_length=255, null=True, blank=True, verbose_name="Órgano interno de control")

    quejas_denuncias = models.TextField(max_length=400, null=True, blank=True,
                                        verbose_name="Datos de contacto para quejas y denuncias")
    inspeccion = models.BooleanField(default=False, null=True, blank=True, verbose_name="¿Es necesaria una inspección y/o verificación?")
    objetivo = models.CharField(max_length=250, null=True, blank=True,
                               verbose_name="Objetivo de la inspección y/o verificación")

    liga_acceso = models.URLField(null=True, blank=True,
                                          verbose_name="Liga de acceso al Registro de Visitar Domiciliarias")
    conservar_informacion = models.CharField(max_length=250, null=True, blank=True,
                                   verbose_name="¿Este trámite o servicio requiere conservar información para fines de acreditación, inspección y verificación con motivo del trámite o servicio?")

    ambito_inspeccion_verificacion = models.ForeignKey(Ambito,on_delete=models.PROTECT,  null=True, blank=True,
                                           related_name="+")
    tipo_inspeccion_verificacion = models.ForeignKey(Tipo,on_delete=models.PROTECT, null=True, blank=True, related_name="+")
    nombre_inspeccion_verificacion = models.CharField(max_length=200, null=True, blank=True, verbose_name="Nombre")
    articulo_vigencia = models.CharField(max_length=50, null=True, blank=True, verbose_name="Artículo")
    fraccion_inspeccion_verificacion = models.CharField(max_length=100, blank=True, null=True, verbose_name="Fracción")

    fundamento_informacion = models.TextField(max_length=300, null=True, blank=True,
                                              verbose_name="Fundamento del requerimiento de conservar información")
    ambito_informacion = models.ForeignKey(Ambito, on_delete=models.PROTECT, null=True, blank=True, related_name="+")
    tipo_informacion = models.ForeignKey(OrdenamientoJuridico, models.PROTECT, null=True, blank=True, related_name="+")
    nombre_informacion = models.TextField(max_length=200, null=True, blank=True, verbose_name="Nombre")
    articulo_informacion = models.CharField(max_length=50, null=True, blank=True, verbose_name="Artículo")
    fraccion_informacion = models.CharField(max_length=100, blank=True, null=True, verbose_name="Fracción")

    registro_regulaciones_canal = models.CharField(max_length=100, blank=True, null=True,
                                                   verbose_name="Registro de regulaciones")

    solicitudes_recibidas = models.IntegerField(null=True, blank=True,
                                                verbose_name="Número de solicitudes recibidas en el año anterior")
    total_solicitudes_recibidas = models.IntegerField(null=True, blank=True,
                                                      verbose_name="Número de solicitudes recibidas")
    informacion = models.CharField(max_length=100, null=True, blank=True,
                                   verbose_name="Información adicional")
    informacion_interesado = models.CharField(max_length=150, null=True, blank=True,
                                              verbose_name="Información que sea útil para que el interesado realice el trámite")
    protesta_ciudadana = models.CharField(max_length=150, null=True, blank=True,
                                              verbose_name="Protesta Ciudadana")
    cantidad_protestas = models.IntegerField(null=True, blank=True,
                                            verbose_name="Cantidad de protestas recibidas en el año")
    momento_vida = models.CharField(max_length=250, null=True, blank=True,
                                       verbose_name="Momentos de vida")

    def __str__(self):
        return self.homoclave

    class Meta:
        ordering = ['homoclave']

    def conversion_bool(self, value):
        if value == False:
            return "No"
        else:
            return "Si"
