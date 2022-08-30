from django.db import models

class Ambito(models.Model):
    nombre = models.CharField(max_length=10)

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
    nombre = models.CharField(max_length=10)

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
    nombre = models.CharField(max_length=50)

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


class Requisito(models.Model):
    nombre = models.CharField(max_length=160, verbose_name="Nombre del requisito")
    original_copia = models.ForeignKey(OriginalCopia, on_delete=models.PROTECT, null=True, blank=True,
                                       verbose_name="Original o copia")
    descripcion = models.CharField(max_length=200, null=True, blank=True, verbose_name="Descripción")

    formato = models.BooleanField(default=False, null=True, blank=True, verbose_name="Forma parte del formato")
    naturaleza = models.CharField(max_length=20, null=True, blank=True, verbose_name="Naturaleza")
    tiempo_promedio = models.IntegerField(null=True, blank=True,
                                          verbose_name="Tiempo promedio en conseguir el requisito para su presentación (horas)")
    firma_validacion = models.BooleanField(default=False, null=True, blank=True,
                                        verbose_name="¿Es necesario alguna firma, validación, certificación, autorización o visto bueno de un tercero?")
    persona_emite = models.CharField(max_length=200, null=True, blank=True,
                                     verbose_name="Nombre de la empresa o persona que lo emite")
    requisito_solicitado = models.CharField(max_length=20, null=True, blank=True,
                                            verbose_name="¿El requisito solicitado es un trámite que se debe realizar con alguna dependencia gubernamental?")
    nombre_dependencia = models.CharField(max_length=100, null=True, blank=True,
                                          verbose_name="Nombre de la dependencia, ubicación y medios de contacto")

    def __str__(self):
        return self.nombre


class DatoGeneral(models.Model):

    homoclave_anterior = models.CharField(max_length=40, blank=True, null=True, verbose_name="Homoclave anterior")
    homoclave = models.CharField(max_length=40, blank=True, null=True, verbose_name="Homoclave")
    nombre_tramite = models.CharField(max_length=150, verbose_name="Nombre del trámite")
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT)
    tipo_tramite = models.ForeignKey(TipoTramite, on_delete=models.PROTECT, verbose_name="Tipo de trámite")
    depedencia = models.CharField(max_length=200, verbose_name="Depedencia")
    unidad_administrativa = models.CharField(max_length=250, verbose_name="Unidad Administrativa")
    nivel_gobierno = models.ForeignKey(NivelDeGobierno, on_delete=models.PROTECT, verbose_name="Nivel de gobierno")
    descripcion = models.TextField(max_length=500, verbose_name="Descripción")
    modalidades = models.ManyToManyField(Modalidad, related_name="Modalidad")

    numero_identificador = models.CharField(max_length=100, blank=True, null=True, verbose_name ="Número de identificador del formato")

    pasos = models.ForeignKey(Paso, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Pasos")

    puede_agendar_cita = models.BooleanField(default=False, verbose_name="¿Es obligatorio agendar una cita?")
    puede_realizar_tramite = models.BooleanField(default=False,
                                                 verbose_name="¿Se puede agendar una cita para realizar un trámite?")
    medio_cita = models.ManyToManyField(Modalidad, verbose_name="Medio para solicitar la cita")

    monto = models.CharField(max_length=100, null=True, blank=True, verbose_name="Monto")
    moneda_pago = models.CharField(max_length=20, verbose_name="Moneda en la que se realiza el pago")
    metodologia_monto = models.TextField(max_length=300, verbose_name="Metodología para cálculo del monto")
    realizar_pago = models.ManyToManyField(UbicacionPago,
                                     verbose_name="¿En dónde puedo realizar el pago?")
    forma_pago = models.ManyToManyField(FormaPago,
                                  verbose_name="Forma de pago")
    etapa_tramite = models.CharField(max_length=100, null=True, blank=True,
                                     verbose_name="Etapa del trámite o servicio en que se realiza o se puede realizar el trámite")
    vigencia_pago = models.CharField(max_length=100, null=True, blank=True,
                                     verbose_name="Vigencia de la línea de captura para realizar el pago en caso de requerirla")

    tiempo_resolucion = models.IntegerField(null=True, blank=True,
                                            verbose_name="Tiempo que tiene la dependencia para resolver")
    plazo_prevenir = models.CharField(max_length=100, null=True, blank=True,
                                      verbose_name="Plazo que tiene la dependencia para prevenir")
    plazo_responder = models.IntegerField(null=True, blank=True,
                                          verbose_name="Plazo que tiene el usuario para responder la prevención")
    derecho_respuesta = models.CharField(max_length=30, null=True, blank=True,
                                         verbose_name="Derecho del usuario ante la falta de respuesta")

    tipo_resolucion = models.ForeignKey(TipoResolucion, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Tipo de resolución")
    vigencia = models.CharField(max_length=100, null=True, blank=True, verbose_name="Vigencia")

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
    resolucion = models.BooleanField(default=False, null=True, blank=True,
                                  verbose_name="La resolución de este trámite está vinculada con la presentación de otros trámites")
    liga_tramite = models.CharField(max_length=200, null=True, blank=True,
                                    verbose_name="Liga del trámite con que está vincualdo")
    resolucion_requisito = models.CharField(max_length=2, null=True, blank=True,
                                            verbose_name="¿La resolución es requisito de otro trámite?")
    liga_resolucion = models.BooleanField(default=False, null=True, blank=True,
                                       verbose_name="Liga de la resolución del trámite")

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
    organo = models.CharField(max_length=100, null=True, blank=True, verbose_name="Órgano interno de control")
    quejas_denuncias = models.TextField(max_length=400, null=True, blank=True,
                                        verbose_name="Datos de contacto para quejas y denuncias")

    fundamento_vigencia = models.TextField(max_length=300, null=True, blank=True,
                                           verbose_name="Fundamento de la vigencia")
    ambito_vigencia = models.CharField(max_length=100, null=True, blank=True, verbose_name="Ámbito")
    tipo_vigencia = models.CharField(max_length=150, null=True, blank=True, verbose_name="Tipo")
    nombre_vigencia = models.TextField(max_length=200, null=True, blank=True, verbose_name="Nombre")
    articulo_vigencia = models.CharField(max_length=50, null=True, blank=True, verbose_name="Artículo")

    fundamento_plazo_maximo = models.TextField(max_length=300, null=True, blank=True,
                                               verbose_name="Fundamento del plazo máximo")
    ambito_plazo_maximo = models.CharField(max_length=100, null=True, blank=True, verbose_name="Ámbito")
    tipo_plazo_maximo = models.CharField(max_length=150, null=True, blank=True, verbose_name="Tipo")
    nombre_plazo_maximo = models.TextField(max_length=200, null=True, blank=True, verbose_name="Nombre")
    articulo_plazo_maximo = models.CharField(max_length=50, null=True, blank=True, verbose_name="Artículo")

    fundamento_informacion = models.TextField(max_length=300, null=True, blank=True,
                                              verbose_name="Fundamento del requerimiento de conservar información")
    ambito_informacion = models.CharField(max_length=100, null=True, blank=True, verbose_name="Ámbito")
    tipo_informacion = models.CharField(max_length=150, null=True, blank=True, verbose_name="Tipo")
    nombre_informacion = models.TextField(max_length=200, null=True, blank=True, verbose_name="Nombre")
    articulo_informacion = models.CharField(max_length=50, null=True, blank=True, verbose_name="Artículo")

    fundamento_inspeccion = models.TextField(max_length=300, null=True, blank=True,
                                             verbose_name="Fundamento de la inspección, verificación o visita domiciliaria")
    ambito_inspeccion = models.CharField(max_length=100, null=True, blank=True, verbose_name="Ámbito")
    tipo_inspeccion = models.CharField(max_length=150, null=True, blank=True, verbose_name="Tipo")
    nombre_inspeccion = models.TextField(max_length=200, null=True, blank=True, verbose_name="Nombre")
    articulo_inspeccion = models.CharField(max_length=50, null=True, blank=True, verbose_name="Artículo")

    fundamento_tramite_servicio = models.TextField(max_length=300, null=True, blank=True,
                                                   verbose_name="Fundamento que da origen al trámite o servicio")
    ambito_tramite_servicio = models.CharField(max_length=100, null=True, blank=True, verbose_name="Ámbito")
    tipo_tramite_servicio = models.CharField(max_length=150, null=True, blank=True, verbose_name="Tipo")
    nombre_tramite_servicio = models.TextField(max_length=200, null=True, blank=True, verbose_name="Nombre")
    articulo_tramite_servicio = models.CharField(max_length=50, null=True, blank=True, verbose_name="Artículo")

    fundamento_criterio = models.TextField(max_length=300, null=True, blank=True,
                                           verbose_name="Fundamento del criterio de resolución")
    ambito_criterio = models.CharField(max_length=100, null=True, blank=True, verbose_name="Ámbito")
    tipo_criterio = models.CharField(max_length=150, null=True, blank=True, verbose_name="Tipo")
    nombre_criterio = models.TextField(max_length=200, null=True, blank=True, verbose_name="Nombre")
    articulo_criterio = models.CharField(max_length=50, null=True, blank=True, verbose_name="Artículo")

    fundamento_derechos = models.TextField(max_length=300, null=True, blank=True,
                                           verbose_name="Fundamento del monto de los derechos")
    ambito_derechos = models.CharField(max_length=100, null=True, blank=True,
                                       verbose_name="Ámbito")
    tipo_derechos = models.CharField(max_length=150, null=True, blank=True,
                                     verbose_name="Tipo")
    nombre_derechos = models.TextField(max_length=200, null=True, blank=True,
                                       verbose_name="Nombre")
    articulo_derechos = models.CharField(max_length=50, null=True, blank=True,
                                         verbose_name="Artículo")

    fundamento_canal = models.TextField(max_length=300, null=True, blank=True,
                                        verbose_name="Fundamento del canal de atención")
    ambito_canal = models.CharField(max_length=100, null=True, blank=True,
                                    verbose_name="Ámbito")
    tipo_canal = models.CharField(max_length=150, null=True, blank=True,
                                  verbose_name="Tipo")
    nombre_canal = models.TextField(max_length=200, null=True, blank=True,
                                    verbose_name="Nombre")
    articulo_canal = models.CharField(max_length=50, null=True, blank=True,
                                      verbose_name="Artículo")
    registro_regulaciones_canal = models.CharField(max_length=100,blank=True, null=True,
                                                   verbose_name="Registro de regulaciones")

    conservar_informacion = models.TextField(null=True, blank=True, max_length=500)
    tramite_informacion = models.TextField(max_length=300, null=True, blank=True,
                                           verbose_name="¿Este trámite o servicio requiere conservar información para fines de acreditación, inspección y verificación con motivo del trámite o servicio?")

    solicitudes_recibidas = models.IntegerField(null=True, blank=True,
                                                verbose_name="Número de solicitudes recibidas en el año anterior")
    total_solicitudes_recibidas = models.IntegerField(null=True, blank=True,
                                                      verbose_name="Número de solicitudes recibidas")

    informacion = models.CharField(max_length=100, null=True, blank=True,
                                   verbose_name="Información adicional")
    informacion_interesado = models.CharField(max_length=150, null=True, blank=True,
                                              verbose_name="Información que sea útil para que el interesado realice el trámite")
    protesta_ciudadana = models.CharField(max_length=100, null=True, blank=True,
                                          verbose_name="Protesta Ciudadana")
    protesta_anual = models.IntegerField(null=True, blank=True,
                                         verbose_name="Cantidad de protestas recibidas al año")

    def __str__(self):
        return self.homoclave
