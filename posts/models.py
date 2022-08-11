from django.db import models

class Dato(models.Model):
    Homoclave = models.CharField(max_length=20, verbose_name="Homoclave")
    NombreTramite = models.CharField(max_length=150, verbose_name="Nombre del trámite")
    Tipo = models.CharField(max_length=30, verbose_name="Tipo")
    TipoTramite = models.CharField(max_length=100, verbose_name="Tipo de trámite")
    Depedencia = models.CharField(max_length=200, verbose_name="Depedencia")
    UnidadAdministrativa = models.TextField(max_length=300, verbose_name="Unidad Administrativa")
    NivelGobierno = models.CharField(max_length=200, verbose_name="Nivel de gobierno")
    Descripcion = models.TextField(max_length=500, verbose_name="Descripción")
    Modalidad = models.CharField(max_length=100, verbose_name="Modalidad")

class Requisito(models.Model):
    Requisitos = models.TextField(max_length=300, blank=True, verbose_name="Requisitos")
    NombreRequisito = models.CharField(max_length=200, blank=True, verbose_name="Nombre del requisito")
    OriginalCopia = models.TextField(max_length=300, blank=True, verbose_name="Original o copia")
    Descripcion = models.TextField(max_length=500, blank=True, verbose_name="Descripción")
    Formato = models.CharField(max_length=20, blank=True, verbose_name="Forma parte del formato")
    Naturaleza = models.CharField(max_length=20, blank=True, verbose_name="Naturaleza")
    TiempoPromedio = models.IntegerField(blank=True, verbose_name="Tiempo promedio en conseguir el requisito para su presentación (días)")
    FirmaValidacion = models.CharField(max_length=20, blank=True, verbose_name="¿Es necesario alguna firma, validación, certificación, autorización o visto bueno de un tercero?" )
    PersonaEmite = models.CharField(max_length=100, blank=True, verbose_name="Nombre de la empresa o persona que lo emite")
    RequisitoSolicitado = models.CharField(max_length=20, blank=True, verbose_name="¿El requisito solicitado es un trámite que se debe realizar con alguna dependencia gubernamental?")
    NombreDependencia = models.CharField(max_length=100, blank=True, verbose_name="Nombre de la dependencia, ubicación y medios de contacto")


class Formato(models.Model):
    NombreFormato = models.CharField(max_length=100, blank=True, verbose_name="Nombre del formato" )
    NumeroIdentificador = models.IntegerField(verbose_name="Número de identificador del formato")

class Paso(models.Model):
    Pasos = models.TextField(max_length=250, blank=True, verbose_name="Pasos")
    Modalidades = models.CharField(max_length=100, verbose_name="Modalidades")

class Cita(models.Model):
    AgendarCita = models.CharField(max_length=2, verbose_name="¿Es obligatorio agendar una cita?")
    RealizarTramite = models.CharField(max_length=2, verbose_name="¿Se puede agendar una cita para realizar un trámite?")
    MedioCita = models.TextField(max_length=500, blank=True, verbose_name="Medio para solicitar la cita")

class Costo(models.Model):
    Monto = models.IntegerField(verbose_name="Monto")
    MonedaPago = models.CharField(max_length=20, verbose_name="Moneda en la que se realiza el pago")
    MetodologiaMonto = models.TextField(max_length=300, verbose_name="Metodología para cálculo del monto")
    RealizarPago = models.TextField(max_length=250, blank=True, verbose_name="¿En dónde puedo realizar el pago?")
    FormaPago = models.CharField(max_length=100, blank=True, verbose_name="Forma de pago")
    EtapaTramite = models.CharField(max_length=100, blank=True, verbose_name="Etapa del trámite o servicio en que se realiza o se puede realizar el trámite")
    VigenciaPago = models.CharField(max_length=30, blank=True, verbose_name="Vigencia de la línea de captura para realizar el pago en caso de requerirla")

class Tiempo(models.Model):
    TiempoResolucion = models.IntegerField(blank=True,verbose_name="Tiempo que tiene la dependencia para resolver")
    PlazoPrevenir = models.CharField(max_length=100, blank=True, verbose_name="Plazo que tiene la dependencia para prevenir")
    PlazoResponder = models.IntegerField(blank=True, verbose_name="Plazo que tiene el usuario para responder la prevención")
    DerechoRespuesta = models.CharField(max_length=30,blank=True, verbose_name="Derecho del usuario ante la falta de respuesta")

class Vigencia(models.Model):
    TipoResolucion = models.CharField(max_length=20, verbose_name="Tipo de resolución")
    Vigencia = models.CharField(max_length=30, blank=True, verbose_name="Vigencia")

class Solicitante(models.Model):
    PersonaSolicitante = models.TextField(max_length=300, verbose_name="¿Quién puede solicitarlo?")
    FuncionalidadTramite = models.TextField(max_length=400, blank=True, verbose_name="¿Para qué sirve realizar este trámite?")
    CasoSolicitud = models.CharField(max_length=150, blank=True, verbose_name="¿En qué caso se debe solicitar el trámite o servicio?")
    ActividadEconomica = models.TextField(max_length=300, blank=True, verbose_name="Actividad económica que está vinculada al trámite o servicio")
    Detalle = models.TextField(max_length=500, blank=True, verbose_name="Detalle")
    Subsector = models.TextField(max_length=350, blank=True, verbose_name="Subsector")
    Rama = models.TextField(max_length=300, blank=True, verbose_name="Rama")
    Subrama = models.CharField(max_length=150, blank=True, verbose_name="Subrama")
    Clase = models.CharField(max_length=200, blank=True, verbose_name="Clase")
    Resolucion = models.TextField(max_length=300, blank=True, verbose_name="La resolución de este trámite está vinculada con la presentación de otros trámites")
    LigaTramite = models.CharField(max_length=200, blank=True, verbose_name="Liga del trámite con que está vincualdo")
    ResolucionRequisito = models.CharField(max_length=2, blank=True, verbose_name="La resolución es requisito de otro trámite")
    LigaResolucion = models.CharField(max_length=100, blank=True, verbose_name="Liga de la resolución del trámite")

class ResponsableResolucion(models.Model):
    ResponsableTramite = models.CharField(max_length=100,blank=True, verbose_name="Responsable del trámite o servicio")
    Nombre = models.CharField(max_length=100, blank=True, verbose_name="Nombre")
    RolFuncionario = models.CharField(max_length=30, blank=True, verbose_name="Rol del funcionario")
    Cargo = models.CharField(max_length=50, blank=True, verbose_name="Cargo")
    CorreoElectronico = models.EmailField(max_length=100, blank=True, verbose_name="Correo electrónico")
    Otro = models.CharField(max_length=30, blank=True, verbose_name="Otro")
    Telefono = models.IntegerField(blank=True, verbose_name="Teléfono")
    Extension = models.IntegerField(blank=True, verbose_name="Extensión")
    DatosResponsable = models.CharField(blank=True, max_length=200, verbose_name="Datos de la oficina del responsable del trámite")
    Organo = models.CharField(max_length=100, blank=True, verbose_name="Órgano interno de control")
    QuejasDenuncias = models.TextField(max_length=400, blank=True, verbose_name="Datos de contacto para quejas y denuncias")

class FundamentoJuridico(models.Model):
    FundamentoVigencia = models.CharField(max_length=150, blank=True, verbose_name="Fundamento de la vigencia")
    Ambito = models.CharField(max_length=100,blank=True, verbose_name="Ámbito")
    Tipo = models.CharField(max_length=150, blank=True, verbose_name="Tipo")
    Nombre = models.TextField(max_length=200, blank=True, verbose_name="Nombre")
    Articulo = models.CharField(max_length=50, blank=True, verbose_name="Artículo")

class FundamentoJuridico2(models.Model):
    FundamentoPlazoMaximo = models.CharField(max_length=150, blank=True, verbose_name="Fundamento del plazo máximo")
    Ambito = models.CharField(max_length=100,blank=True, verbose_name="Ámbito")
    Tipo = models.CharField(max_length=150, blank=True, verbose_name="Tipo")
    Nombre = models.TextField(max_length=200, blank=True, verbose_name="Nombre")
    Articulo = models.CharField(max_length=50, blank=True, verbose_name="Artículo")

class FundamentoJuridico3(models.Model):
    FundamentoInformacion = models.CharField(max_length=150, blank=True, verbose_name="Fundamento del requerimiento de conservar información")
    Ambito = models.CharField(max_length=100,blank=True, verbose_name="Ámbito")
    Tipo = models.CharField(max_length=150, blank=True, verbose_name="Tipo")
    Nombre = models.TextField(max_length=200, blank=True, verbose_name="Nombre")
    Articulo = models.CharField(max_length=50, blank=True, verbose_name="Artículo")


class FundamentoJuridico4(models.Model):
    FundamentoInspeccion= models.CharField(max_length=150, blank=True, verbose_name="Fundamento de la inspección, verificación o visita domiciliaria")
    Ambito = models.CharField(max_length=100,blank=True, verbose_name="Ámbito")
    Tipo = models.CharField(max_length=150, blank=True, verbose_name="Tipo")
    Nombre = models.TextField(max_length=200, blank=True, verbose_name="Nombre")
    Articulo = models.CharField(max_length=50, blank=True, verbose_name="Artículo")


class FundamentoJuridico5(models.Model):
    FundamentoTramiteOServicio = models.CharField(max_length=150, blank=True, verbose_name="Fundamento que da origen al trámite o servicio")
    Ambito = models.CharField(max_length=100,blank=True, verbose_name="Ámbito")
    Tipo = models.CharField(max_length=150, blank=True, verbose_name="Tipo")
    Nombre = models.TextField(max_length=200, blank=True, verbose_name="Nombre")
    Articulo = models.CharField(max_length=50, blank=True, verbose_name="Artículo")

class FundamentoJuridico6(models.Model):
    FundamentoCriterio= models.CharField(max_length=150, blank=True, verbose_name="Fundamento del criterio de resolución")
    Ambito = models.CharField(max_length=100,blank=True, verbose_name="Ámbito")
    Tipo = models.CharField(max_length=150, blank=True, verbose_name="Tipo")
    Nombre = models.TextField(max_length=200, blank=True, verbose_name="Nombre")
    Articulo = models.CharField(max_length=50, blank=True, verbose_name="Artículo")

class FundamentoJuridico7(models.Model):
    FundamentoDerechos = models.CharField(max_length=150, blank=True, verbose_name="Fundamento del monto de los derechos")
    Ambito = models.CharField(max_length=100,blank=True, verbose_name="Ámbito")
    Tipo = models.CharField(max_length=150, blank=True, verbose_name="Tipo")
    Nombre = models.TextField(max_length=200, blank=True, verbose_name="Nombre")
    Articulo = models.CharField(max_length=50, blank=True, verbose_name="Artículo")

class FundamentoJuridico8(models.Model):
    FundamentoCanal= models.CharField(max_length=150, blank=True, verbose_name="Fundamento del canal de atención")
    Ambito = models.CharField(max_length=100,blank=True, verbose_name="Ámbito")
    Tipo = models.CharField(max_length=150, blank=True, verbose_name="Tipo")
    Nombre = models.TextField(max_length=200, blank=True, verbose_name="Nombre")
    Articulo = models.CharField(max_length=50, blank=True, verbose_name="Artículo")
    RegristroRegulaciones = models.CharField(max_length=100, verbose_name="Registro de regulaciones")

class Inspeccion(models.Model):
    ConservarInformacion = models.TextField(blank=True, max_length=500)
    TramiteInformacion = models.TextField(max_length=300, blank=True, verbose_name="¿Este trámite o servicio requiere conservar información para fines de acreditación, inspección y verificación con motivo del trámite o servicio?")


class Estadistica(models.Model):
    solicitudesRecibidas = models.IntegerField(blank=True, verbose_name="Número de solicitudes recibidas en el año anterior")
    TotalSolicitudesRecibidas = models.IntegerField(blank=True, verbose_name="Número de solicitudes recibidas")

class InformacionAdicional(models.Model):
    Informacion = models.CharField(max_length=100, blank=True, verbose_name="Información adicional")
    InformacionInteresado = models.CharField(max_length=150, blank=True, verbose_name="Información que sea útil para que el interesado realice el trámite")
    ProtestaCiudadana = models.CharField(max_length=100, blank=True, verbose_name="Protesta Ciudadana")
    ProtestasAnual = models.IntegerField(blank=True, verbose_name="Cantidad de protestas recibidas al año")

# Create your models here.
