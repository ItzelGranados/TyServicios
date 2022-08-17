# Generated by Django 4.1 on 2022-08-16 18:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_rename_ambito_fundamentojuridico6_ambito_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ambito',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='DatoGeneral',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('homoclave', models.CharField(max_length=20, verbose_name='Homoclave')),
                ('nombre_tramite', models.CharField(max_length=150, verbose_name='Nombre del trámite')),
                ('tipo_tramite', models.CharField(max_length=100, verbose_name='Tipo de trámite')),
                ('depedencia', models.CharField(max_length=200, verbose_name='Depedencia')),
                ('unidad_administrativa', models.TextField(max_length=300, verbose_name='Unidad Administrativa')),
                ('nivel_gobierno', models.CharField(max_length=200, verbose_name='Nivel de gobierno')),
                ('modalidad', models.CharField(max_length=100, verbose_name='Modalidad')),
                ('nombre_requisito', models.CharField(blank=True, max_length=200, verbose_name='Nombre del requisito')),
                ('OriginalCopia', models.CharField(blank=True, max_length=50, verbose_name='Original o copia')),
                ('descripcion', models.TextField(blank=True, max_length=500, verbose_name='Descripción')),
                ('formato', models.CharField(blank=True, max_length=20, verbose_name='Forma parte del formato')),
                ('naturaleza', models.CharField(blank=True, max_length=20, verbose_name='Naturaleza')),
                ('tiempo_promedio', models.IntegerField(blank=True, verbose_name='Tiempo promedio en conseguir el requisito para su presentación (horas)')),
                ('firma_validacion', models.CharField(blank=True, max_length=20, verbose_name='¿Es necesario alguna firma, validación, certificación, autorización o visto bueno de un tercero?')),
                ('persona_emite', models.CharField(blank=True, max_length=100, verbose_name='Nombre de la empresa o persona que lo emite')),
                ('requisito_solicitado', models.CharField(blank=True, max_length=20, verbose_name='¿El requisito solicitado es un trámite que se debe realizar con alguna dependencia gubernamental?')),
                ('nombre_dependencia', models.CharField(blank=True, max_length=100, verbose_name='Nombre de la dependencia, ubicación y medios de contacto')),
                ('nombre_formato', models.CharField(blank=True, max_length=100, verbose_name='Nombre del formato')),
                ('numero_identificador', models.IntegerField(verbose_name='Número de identificador del formato')),
                ('pasos', models.TextField(blank=True, max_length=250, verbose_name='Pasos')),
                ('modalidades', models.CharField(max_length=100, verbose_name='Modalidades')),
                ('agendar_cita', models.CharField(max_length=2, verbose_name='¿Es obligatorio agendar una cita?')),
                ('realizar_tramite', models.CharField(max_length=2, verbose_name='¿Se puede agendar una cita para realizar un trámite?')),
                ('medio_cita', models.TextField(blank=True, max_length=500, verbose_name='Medio para solicitar la cita')),
                ('monto', models.IntegerField(verbose_name='Monto')),
                ('moneda_pago', models.CharField(max_length=20, verbose_name='Moneda en la que se realiza el pago')),
                ('metodologia_monto', models.TextField(max_length=300, verbose_name='Metodología para cálculo del monto')),
                ('realizar_pago', models.TextField(blank=True, max_length=250, verbose_name='¿En dónde puedo realizar el pago?')),
                ('forma_pago', models.CharField(blank=True, max_length=100, verbose_name='Forma de pago')),
                ('etapa_tramite', models.CharField(blank=True, max_length=100, verbose_name='Etapa del trámite o servicio en que se realiza o se puede realizar el trámite')),
                ('vigencia_pago', models.CharField(blank=True, max_length=30, verbose_name='Vigencia de la línea de captura para realizar el pago en caso de requerirla')),
                ('tiempo_resolucion', models.IntegerField(blank=True, verbose_name='Tiempo que tiene la dependencia para resolver')),
                ('plazo_prevenir', models.CharField(blank=True, max_length=100, verbose_name='Plazo que tiene la dependencia para prevenir')),
                ('plazo_responder', models.IntegerField(blank=True, verbose_name='Plazo que tiene el usuario para responder la prevención')),
                ('derecho_respuesta', models.CharField(blank=True, max_length=30, verbose_name='Derecho del usuario ante la falta de respuesta')),
                ('tipo_resolucion', models.CharField(max_length=20, verbose_name='Tipo de resolución')),
                ('vigencia', models.CharField(blank=True, max_length=30, verbose_name='Vigencia')),
                ('persona_solicitante', models.TextField(max_length=300, verbose_name='¿Quién puede solicitarlo?')),
                ('funcionalidad_tramite', models.TextField(blank=True, max_length=400, verbose_name='¿Para qué sirve realizar este trámite?')),
                ('caso_solicitud', models.CharField(blank=True, max_length=150, verbose_name='¿En qué caso se debe solicitar el trámite o servicio?')),
                ('actividad_economica', models.TextField(blank=True, max_length=300, verbose_name='Actividad económica que está vinculada al trámite o servicio')),
                ('detalle', models.TextField(blank=True, max_length=500, verbose_name='Detalle')),
                ('subsector', models.TextField(blank=True, max_length=350, verbose_name='Subsector')),
                ('rama', models.TextField(blank=True, max_length=300, verbose_name='Rama')),
                ('subrama', models.CharField(blank=True, max_length=150, verbose_name='Subrama')),
                ('clase', models.CharField(blank=True, max_length=200, verbose_name='Clase')),
                ('resolucion', models.TextField(blank=True, max_length=300, verbose_name='La resolución de este trámite está vinculada con la presentación de otros trámites')),
                ('liga_tramite', models.CharField(blank=True, max_length=200, verbose_name='Liga del trámite con que está vincualdo')),
                ('resolucion_requisito', models.CharField(blank=True, max_length=2, verbose_name='La resolución es requisito de otro trámite')),
                ('liga_resolucion', models.CharField(blank=True, max_length=100, verbose_name='Liga de la resolución del trámite')),
                ('responsable_tramite', models.CharField(blank=True, max_length=100, verbose_name='Responsable del trámite o servicio')),
                ('rol_funcionario', models.CharField(blank=True, max_length=30, verbose_name='Rol del funcionario')),
                ('cargo', models.CharField(blank=True, max_length=50, verbose_name='Cargo')),
                ('correo_electronico', models.EmailField(blank=True, max_length=100, verbose_name='Correo electrónico')),
                ('otro', models.CharField(blank=True, max_length=30, verbose_name='Otro')),
                ('telefono', models.IntegerField(blank=True, verbose_name='Teléfono')),
                ('extension', models.IntegerField(blank=True, verbose_name='Extensión')),
                ('datos_responsable', models.CharField(blank=True, max_length=200, verbose_name='Datos de la oficina del responsable del trámite')),
                ('organo', models.CharField(blank=True, max_length=100, verbose_name='Órgano interno de control')),
                ('quejas_denuncias', models.TextField(blank=True, max_length=400, verbose_name='Datos de contacto para quejas y denuncias')),
                ('fundamento_vigencia', models.CharField(blank=True, max_length=150, verbose_name='Fundamento de la vigencia')),
                ('fundamento_plazoMaximo', models.CharField(blank=True, max_length=150, verbose_name='Fundamento del plazo máximo')),
                ('fundamento_informacion', models.CharField(blank=True, max_length=150, verbose_name='Fundamento del requerimiento de conservar información')),
                ('fundamento_inspeccion', models.CharField(blank=True, max_length=150, verbose_name='Fundamento de la inspección, verificación o visita domiciliaria')),
                ('fundamentoTramiteOServicio', models.CharField(blank=True, max_length=150, verbose_name='Fundamento que da origen al trámite o servicio')),
                ('fundamentoCriterio', models.CharField(blank=True, max_length=150, verbose_name='Fundamento del criterio de resolución')),
                ('fundamento_derechos', models.CharField(blank=True, max_length=150, verbose_name='Fundamento del monto de los derechos')),
                ('fundamento_canal', models.CharField(blank=True, max_length=150, verbose_name='Fundamento del canal de atención')),
                ('ambito', models.CharField(blank=True, max_length=100, verbose_name='Ámbito')),
                ('tipo', models.CharField(blank=True, max_length=150, verbose_name='Tipo')),
                ('nombre', models.TextField(blank=True, max_length=200, verbose_name='Nombre')),
                ('articulo', models.CharField(blank=True, max_length=50, verbose_name='Artículo')),
                ('regristro_regulaciones', models.CharField(max_length=100, verbose_name='Registro de regulaciones')),
                ('conservar_informacion', models.TextField(blank=True, max_length=500)),
                ('tramite_informacion', models.TextField(blank=True, max_length=300, verbose_name='¿Este trámite o servicio requiere conservar información para fines de acreditación, inspección y verificación con motivo del trámite o servicio?')),
                ('solicitudes_recibidas', models.IntegerField(blank=True, verbose_name='Número de solicitudes recibidas en el año anterior')),
                ('total_solicitudes_recibidas', models.IntegerField(blank=True, verbose_name='Número de solicitudes recibidas')),
                ('informacion', models.CharField(blank=True, max_length=100, verbose_name='Información adicional')),
                ('informacion_interesado', models.CharField(blank=True, max_length=150, verbose_name='Información que sea útil para que el interesado realice el trámite')),
                ('protesta_ciudadana', models.CharField(blank=True, max_length=100, verbose_name='Protesta Ciudadana')),
                ('protesta_anual', models.IntegerField(blank=True, verbose_name='Cantidad de protestas recibidas al año')),
            ],
        ),
        migrations.CreateModel(
            name='FormaPago',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Modalidad',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='NivelDeGobierno',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='OrdenamientoJuridico',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='OriginalCopia',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pasos',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SINO',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TipoResolucion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TipoSolicitante',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TipoTramite',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='UbicacionesPago',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Cita',
        ),
        migrations.DeleteModel(
            name='Costo',
        ),
        migrations.DeleteModel(
            name='Dato',
        ),
        migrations.DeleteModel(
            name='Estadistica',
        ),
        migrations.DeleteModel(
            name='Formato',
        ),
        migrations.DeleteModel(
            name='FundamentoJuridico',
        ),
        migrations.DeleteModel(
            name='FundamentoJuridico2',
        ),
        migrations.DeleteModel(
            name='FundamentoJuridico3',
        ),
        migrations.DeleteModel(
            name='FundamentoJuridico4',
        ),
        migrations.DeleteModel(
            name='FundamentoJuridico5',
        ),
        migrations.DeleteModel(
            name='FundamentoJuridico6',
        ),
        migrations.DeleteModel(
            name='FundamentoJuridico7',
        ),
        migrations.DeleteModel(
            name='FundamentoJuridico8',
        ),
        migrations.DeleteModel(
            name='InformacionAdicional',
        ),
        migrations.DeleteModel(
            name='Inspeccion',
        ),
        migrations.DeleteModel(
            name='Paso',
        ),
        migrations.DeleteModel(
            name='Requisito',
        ),
        migrations.DeleteModel(
            name='ResponsableResolucion',
        ),
        migrations.DeleteModel(
            name='Solicitante',
        ),
        migrations.DeleteModel(
            name='Tiempo',
        ),
        migrations.DeleteModel(
            name='Vigencia',
        ),
    ]
