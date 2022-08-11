from django.db import models


class Dato(models.Model):
    homoclave = models.CharField(max_length=20, verbose_name="Homoclave")
    nombre_tramite = models.CharField(max_length=150, verbose_name="Nombre del trámite")
    tipo = models.CharField(max_length=30, verbose_name="Tipo")
    tipo_tramite = models.CharField(max_length=100, verbose_name="Tipo de trámite")
    depedencia = models.CharField(max_length=200, verbose_name="Depedencia")
    unidad_administrativa = models.TextField(max_length=300, verbose_name="Unidad Administrativa")
    nivel_gobierno = models.CharField(max_length=200, verbose_name="Nivel de gobierno")
    descripcion = models.TextField(max_length=500, verbose_name="Descripción")
    modalidad = models.CharField(max_length=100, verbose_name="Modalidad")

    def __str__(self):
        return self.nombre_tramite


class Requisito(models.Model):
    requisitos = models.TextField(max_length=300, blank=True, verbose_name="Requisitos")
    nombre_requisito = models.CharField(max_length=200, blank=True, verbose_name="Nombre del requisito")
    OriginalCopia = models.TextField(max_length=300, blank=True, verbose_name="Original o copia")
    descripcion = models.TextField(max_length=500, blank=True, verbose_name="Descripción")
    formato = models.CharField(max_length=20, blank=True, verbose_name="Forma parte del formato")
    naturaleza = models.CharField(max_length=20, blank=True, verbose_name="Naturaleza")
    tiempo_promedio = models.IntegerField(blank=True, verbose_name="Tiempo promedio en conseguir el requisito para su presentación (días)")
    firma_validacion = models.CharField(max_length=20, blank=True, verbose_name="¿Es necesario alguna firma, validación, certificación, autorización o visto bueno de un tercero?" )
    persona_emite = models.CharField(max_length=100, blank=True, verbose_name="Nombre de la empresa o persona que lo emite")
    requisito_solicitado = models.CharField(max_length=20, blank=True, verbose_name="¿El requisito solicitado es un trámite que se debe realizar con alguna dependencia gubernamental?")
    nombre_dependencia = models.CharField(max_length=100, blank=True, verbose_name="Nombre de la dependencia, ubicación y medios de contacto")

    def __str__(self):
        return self.requisitos


class Formato(models.Model):
    nombre_formato = models.CharField(max_length=100, blank=True, verbose_name="Nombre del formato")
    numero_identificador = models.IntegerField(verbose_name="Número de identificador del formato")

    def __str__(self):
        return self.nombre_formato




class Paso(models.Model):
    pasos = models.TextField(max_length=250, blank=True, verbose_name="Pasos")
    modalidades = models.CharField(max_length=100, verbose_name="Modalidades")

    def __str__(self):
        return self.pasos


class Cita(models.Model):
    agendar_cita = models.CharField(max_length=2, verbose_name="¿Es obligatorio agendar una cita?")
    realizar_tramite = models.CharField(max_length=2, verbose_name="¿Se puede agendar una cita para realizar un trámite?")
    medio_cita = models.TextField(max_length=500, blank=True, verbose_name="Medio para solicitar la cita")

    def __str__(self):
        return self.agendar_cita

class Costo(models.Model):
    monto = models.IntegerField(verbose_name="Monto")
    moneda_pago = models.CharField(max_length=20, verbose_name="Moneda en la que se realiza el pago")
    metodologia_monto = models.TextField(max_length=300, verbose_name="Metodología para cálculo del monto")
    realizar_pago = models.TextField(max_length=250, blank=True, verbose_name="¿En dónde puedo realizar el pago?")
    forma_pago = models.CharField(max_length=100, blank=True, verbose_name="Forma de pago")
    etapa_tramite = models.CharField(max_length=100, blank=True, verbose_name="Etapa del trámite o servicio en que se realiza o se puede realizar el trámite")
    vigencia_pago = models.CharField(max_length=30, blank=True, verbose_name="Vigencia de la línea de captura para realizar el pago en caso de requerirla")

    def __str__(self):
        return self.monto

class Tiempo(models.Model):
    tiempo_resolucion = models.IntegerField(blank=True,verbose_name="Tiempo que tiene la dependencia para resolver")
    plazo_prevenir = models.CharField(max_length=100, blank=True, verbose_name="Plazo que tiene la dependencia para prevenir")
    plazo_responder = models.IntegerField(blank=True, verbose_name="Plazo que tiene el usuario para responder la prevención")
    derecho_respuesta = models.CharField(max_length=30,blank=True, verbose_name="Derecho del usuario ante la falta de respuesta")

    def __str__(self):
        return self.tiempo_resolucion

class Vigencia(models.Model):
    tipo_resolucion = models.CharField(max_length=20, verbose_name="Tipo de resolución")
    vigencia = models.CharField(max_length=30, blank=True, verbose_name="Vigencia")

    def __str__(self):
        return self.vigencia


class Solicitante(models.Model):
    persona_solicitante = models.TextField(max_length=300, verbose_name="¿Quién puede solicitarlo?")
    funcionalidad_tramite = models.TextField(max_length=400, blank=True, verbose_name="¿Para qué sirve realizar este trámite?")
    caso_solicitud = models.CharField(max_length=150, blank=True, verbose_name="¿En qué caso se debe solicitar el trámite o servicio?")
    actividad_economica = models.TextField(max_length=300, blank=True, verbose_name="Actividad económica que está vinculada al trámite o servicio")
    detalle = models.TextField(max_length=500, blank=True, verbose_name="Detalle")
    subsector = models.TextField(max_length=350, blank=True, verbose_name="Subsector")
    rama = models.TextField(max_length=300, blank=True, verbose_name="Rama")
    subrama = models.CharField(max_length=150, blank=True, verbose_name="Subrama")
    clase = models.CharField(max_length=200, blank=True, verbose_name="Clase")
    resolucion = models.TextField(max_length=300, blank=True, verbose_name="La resolución de este trámite está vinculada con la presentación de otros trámites")
    liga_tramite = models.CharField(max_length=200, blank=True, verbose_name="Liga del trámite con que está vincualdo")
    resolucion_requisito = models.CharField(max_length=2, blank=True, verbose_name="La resolución es requisito de otro trámite")
    liga_resolucion = models.CharField(max_length=100, blank=True, verbose_name="Liga de la resolución del trámite")

    def __str__(self):
        return self.persona_solicitante


class ResponsableResolucion(models.Model):
    responsable_tramite = models.CharField(max_length=100,blank=True, verbose_name="Responsable del trámite o servicio")
    nombre = models.CharField(max_length=100, blank=True, verbose_name="Nombre")
    rol_funcionario = models.CharField(max_length=30, blank=True, verbose_name="Rol del funcionario")
    cargo = models.CharField(max_length=50, blank=True, verbose_name="Cargo")
    correo_electronico = models.EmailField(max_length=100, blank=True, verbose_name="Correo electrónico")
    otro = models.CharField(max_length=30, blank=True, verbose_name="Otro")
    telefono = models.IntegerField(blank=True, verbose_name="Teléfono")
    extension = models.IntegerField(blank=True, verbose_name="Extensión")
    datos_responsable = models.CharField(blank=True, max_length=200, verbose_name="Datos de la oficina del responsable del trámite")
    organo = models.CharField(max_length=100, blank=True, verbose_name="Órgano interno de control")
    quejas_denuncias = models.TextField(max_length=400, blank=True, verbose_name="Datos de contacto para quejas y denuncias")

    def __str__(self):
        return self.responsable_tramite


class FundamentoJuridico(models.Model):
    fundamento_vigencia = models.CharField(max_length=150, blank=True, verbose_name="Fundamento de la vigencia")
    ambito = models.CharField(max_length=100,blank=True, verbose_name="Ámbito")
    tipo = models.CharField(max_length=150, blank=True, verbose_name="Tipo")
    nombre = models.TextField(max_length=200, blank=True, verbose_name="Nombre")
    articulo = models.CharField(max_length=50, blank=True, verbose_name="Artículo")

    def __str__(self):
        return self.fundamento_vigencia


class FundamentoJuridico2(models.Model):
    fundamento_plazoMaximo = models.CharField(max_length=150, blank=True, verbose_name="Fundamento del plazo máximo")
    ambito = models.CharField(max_length=100,blank=True, verbose_name="Ámbito")
    tipo = models.CharField(max_length=150, blank=True, verbose_name="Tipo")
    nombre = models.TextField(max_length=200, blank=True, verbose_name="Nombre")
    articulo = models.CharField(max_length=50, blank=True, verbose_name="Artículo")

    def __str__(self):
        return self.fundamento_plazoMaximo


class FundamentoJuridico3(models.Model):
    fundamento_informacion = models.CharField(max_length=150, blank=True, verbose_name="Fundamento del requerimiento de conservar información")
    ambito = models.CharField(max_length=100,blank=True, verbose_name="Ámbito")
    tipo = models.CharField(max_length=150, blank=True, verbose_name="Tipo")
    nombre = models.TextField(max_length=200, blank=True, verbose_name="Nombre")
    articulo = models.CharField(max_length=50, blank=True, verbose_name="Artículo")

    def __str__(self):
        return self.fundamento_informacion


class FundamentoJuridico4(models.Model):
    fundamento_inspeccion= models.CharField(max_length=150, blank=True, verbose_name="Fundamento de la inspección, verificación o visita domiciliaria")
    ambito = models.CharField(max_length=100,blank=True, verbose_name="Ámbito")
    tipo = models.CharField(max_length=150, blank=True, verbose_name="Tipo")
    nombre = models.TextField(max_length=200, blank=True, verbose_name="Nombre")
    articulo = models.CharField(max_length=50, blank=True, verbose_name="Artículo")

    def __str__(self):
        return self.fundamento_inspeccion


class FundamentoJuridico5(models.Model):
    fundamentoTramiteOServicio = models.CharField(max_length=150, blank=True, verbose_name="Fundamento que da origen al trámite o servicio")
    ambito = models.CharField(max_length=100,blank=True, verbose_name="Ámbito")
    tipo = models.CharField(max_length=150, blank=True, verbose_name="Tipo")
    nombre = models.TextField(max_length=200, blank=True, verbose_name="Nombre")
    articulo = models.CharField(max_length=50, blank=True, verbose_name="Artículo")

    def __str__(self):
        return self.fundamentoTramiteOServicio


class FundamentoJuridico6(models.Model):
    fundamentoCriterio= models.CharField(max_length=150, blank=True, verbose_name="Fundamento del criterio de resolución")
    ambito = models.CharField(max_length=100,blank=True, verbose_name="Ámbito")
    tipo = models.CharField(max_length=150, blank=True, verbose_name="Tipo")
    nombre = models.TextField(max_length=200, blank=True, verbose_name="Nombre")
    articulo = models.CharField(max_length=50, blank=True, verbose_name="Artículo")

    def __str__(self):
        return self.fundamentoCriterio


class FundamentoJuridico7(models.Model):
    fundamento_derechos = models.CharField(max_length=150, blank=True, verbose_name="Fundamento del monto de los derechos")
    ambito = models.CharField(max_length=100,blank=True, verbose_name="Ámbito")
    tipo = models.CharField(max_length=150, blank=True, verbose_name="Tipo")
    nombre = models.TextField(max_length=200, blank=True, verbose_name="Nombre")
    articulo = models.CharField(max_length=50, blank=True, verbose_name="Artículo")

    def __str__(self):
        return self.fundamento_derechos


class FundamentoJuridico8(models.Model):
    fundamento_canal = models.CharField(max_length=150, blank=True, verbose_name="Fundamento del canal de atención")
    ambito = models.CharField(max_length=100,blank=True, verbose_name="Ámbito")
    tipo = models.CharField(max_length=150, blank=True, verbose_name="Tipo")
    nombre = models.TextField(max_length=200, blank=True, verbose_name="Nombre")
    articulo = models.CharField(max_length=50, blank=True, verbose_name="Artículo")
    regristro_regulaciones = models.CharField(max_length=100, verbose_name="Registro de regulaciones")

    def __str__(self):
        return self.fundamento_canal


class Inspeccion(models.Model):
    conservar_informacion = models.TextField(blank=True, max_length=500)
    tramite_informacion = models.TextField(max_length=300, blank=True, verbose_name="¿Este trámite o servicio requiere conservar información para fines de acreditación, inspección y verificación con motivo del trámite o servicio?")

    def __str__(self):
        return self.conservar_informacion


class Estadistica(models.Model):
    solicitudes_recibidas = models.IntegerField(blank=True, verbose_name="Número de solicitudes recibidas en el año anterior")
    total_solicitudes_recibidas = models.IntegerField(blank=True, verbose_name="Número de solicitudes recibidas")

    def __str__(self):
        return  self.solicitudes_recibidas


class InformacionAdicional(models.Model):
    informacion = models.CharField(max_length=100, blank=True, verbose_name="Información adicional")
    informacion_interesado = models.CharField(max_length=150, blank=True, verbose_name="Información que sea útil para que el interesado realice el trámite")
    protesta_ciudadana = models.CharField(max_length=100, blank=True, verbose_name="Protesta Ciudadana")
    protesta_anual = models.IntegerField(blank=True, verbose_name="Cantidad de protestas recibidas al año")

    def __str__(self):
        return self.informacion
# Create your models here.
