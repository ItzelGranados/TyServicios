from django.db import models

class Dato(models.Model):
    Homoclave = models.CharField(max_length=20)
    NombreTramite = models.CharField(max_length=150)
    Tipo = models.CharField(max_length=30)
    TipoTramite = models.CharField(max_length=100)
    Depedencia = models.CharField(max_length=200)
    UnidadAdministrativa = models.CharField(max_length=300)
    NivelGobierno = models.CharField(max_length=200)
    Descripcion = models.TextField(max_length=500)
    Modalidad = models.CharField(max_length=200)

class Requisito(models.Model):
    Requisitos = models.CharField(max_length=300)
    NombreRequisito = models.CharField(max_length=200)
    OriginalCopia = models.CharField(max_length=300)
    Descripcion = models.CharField(max_length=500)
    Formato = models.CharField(max_length=20)
    Naturaleza = models.CharField(max_length=20)
    TiempoPromedio = models.FloatField(max_length=4)
    FirmaValidacion = models.CharField(max_length=3)
    PersonaEmite = models.CharField(max_length=100)
    RequisitoSolicitado = models.CharField(max_length=20)
    NombreDependencia = models.CharField(max_length=100)

class Formato(models.Model):
    NombreFormato = models.CharField(max_length=100)
    NumeroIdentificador = models.IntegerField(max_length=9)

class Paso(models.Model):
    Pasos = models.TextField(max_length=100)
    Modalidades = models.CharField(max_length=100)

class Cita(models.Model):
    AgendarCita = models.CharField(max_length=2)
    RealizarTramite = models.CharField(max_length=2)
    MedioCita = models.CharField(max_length=500)

class Costo(models.Model):
    Monto = models.IntegerField()
    MonedaPago = models.CharField(max_length=20)
    MetodologiaMonto = models.CharField(max_length=300)
    RealizarPago = models.CharField(max_length=250)
    FormaPago = models.CharField(max_length=100)
    EtapaTramite = models.CharField(max_length=100)
    VigenciaPago = models.DateTimeField()

class Tiempo(models.Model):
    TiempoResolucion = models.IntegerField()
    PlazoPrevenir = models.CharField(max_length=100)
    PlazoResponder = models.IntegerField()
    DerechoRespuesta = models.CharField(max_length=30)

class Vigencia(models.Model):
    TipoResolucion = models.CharField(max_length=20)
    Vigencia = models.DateTimeField()

class Solicitante(models.Model):
    PersonaSolicitante = models.CharField(max_length=300)
    FuncionalidadTramite = models.CharField(max_length=400)
    CasoSolicitud = models.CharField(max_length=150)
    ActividadEconomica = models.CharField(max_length=300)
    Detalle = models.CharField(max_length=500)
    Subsector = models.CharField(max_length=350)
    Rama = models.CharField(max_length=300)
    Subrama = models.CharField(max_length=150)
    Clase = models.CharField(max_length=200)
    Resolucion = models.CharField(max_length=300)
    LigaTramite = models.CharField(max_length=200)
    ResolucionRequisito = models.CharField(max_length=2)
    LigaResolucion = models.CharField(max_length=100)

class ResponsableResolucion(models.Model):
    ResponsableTramite = models.CharField(max_length=100)
    Nombre = models.CharField(max_length=100)
    RolFuncionario = models.CharField(max_length=30)
    Cargo = models.CharField(max_length=50)
    CorreoElectronico = models.CharField(max_length=60)
    Otro = models.CharField(max_length=30)
    Telefono = models.IntegerField()
    Extension = models.IntegerField()
    DatosResponsable = models.CharField(max_length=200)
    QuejasDenuncias = models.CharField(max_length=400)

class FundamentoJuridico(models.Model):
    FundamentoVigencia = models.CharField(max_length=150)
    Ambito = models.CharField(max_length=100)
    Tipo = models.CharField(max_length=150)
    Nombre = models.CharField(max_length=200)
    Articulo = models.CharField(max_length=50)

class FundamentoJuridico2(models.Model):
    FundamentoPlazoMaximo = models.CharField(max_length=150)
    Ambito = models.CharField(max_length=100)
    Tipo = models.CharField(max_length=150)
    Nombre = models.CharField(max_length=200)
    Articulo = models.CharField(max_length=50)

class FundamentoJuridico3(models.Model):
    FundamentoInformacion = models.CharField(max_length=150)
    Ambito = models.CharField(max_length=100)
    Tipo = models.CharField(max_length=150)
    Nombre = models.CharField(max_length=200)
    Articulo = models.CharField(max_length=50)

class FundamentoJuridico4(models.Model):
    FundamentoInspeccion = models.CharField(max_length=150)
    Ambito = models.CharField(max_length=100)
    Tipo = models.CharField(max_length=150)
    Nombre = models.CharField(max_length=200)
    Articulo = models.CharField(max_length=50)

class FundamentoJuridico5(models.Model):
    FundamentoTramiteOServicio = models.CharField(max_length=150)
    Ambito = models.CharField(max_length=100)
    Tipo = models.CharField(max_length=150)
    Nombre = models.CharField(max_length=200)
    Articulo = models.CharField(max_length=50)

class FundamentoJuridico6(models.Model):
    FundamentoCriterio = models.CharField(max_length=150)
    Ambito = models.CharField(max_length=100)
    Tipo = models.CharField(max_length=150)
    Nombre = models.CharField(max_length=200)
    Articulo = models.CharField(max_length=50)

class FundamentoJuridico7(models.Model):
    FundamentoDerechos = models.CharField(max_length=150)
    Ambito = models.CharField(max_length=100)
    Tipo = models.CharField(max_length=150)
    Nombre = models.CharField(max_length=200)
    Articulo = models.CharField(max_length=50)

class FundamentoJuridico8(models.Model):
    FundamentoCanal = models.CharField(max_length=150)
    Ambito = models.CharField(max_length=100)
    Tipo = models.CharField(max_length=150)
    Nombre = models.CharField(max_length=200)
    Articulo = models.CharField(max_length=50)
    RegristroRegulaciones = models.CharField(max_length=100)

class Inspeccione(models.Model):
    ConservarInformacion = models.CharField(max_length=500)
    TramiteInformacion = models.CharField(max_length=300)


class Estadistica(models.Model):
    solicitudesRecibidas = models.IntegerField(max_length=10)
    TotalSolicitudesRecibidas = models.IntegerField(max_length=10)

class InformacionAdicional(models.Model):
    Informacion = models.CharField(max_length=100)
    InformacionInteresado = models.CharField(max_length=150)
    ProtestaCiudadana = models.CharField(max_length=100)
    ProtestasAnual = models.IntegerField(max_length=10)

# Create your models here.
