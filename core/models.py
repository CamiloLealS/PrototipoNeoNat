from django.db import models

# Create your models here.
class matrona(models.Model):
        id_usuario = models.IntegerField(primary_key=True)
        username = models.CharField(max_length=50, null=True, unique=True)
        id_superior = models.IntegerField(blank=True,null=True)
        nombre = models.TextField(max_length=50)
        paterno = models.TextField(max_length=50)
        materno = models.TextField(max_length=50, blank=True ,null=True)

        def __str__(self) -> str:
               return self.nombre+ ' ' + self.paterno + ' ' +str(self.id_usuario)

class matrona_clinica(matrona):
        def __str__(self) -> str:
               return 'Matrona Clínica '+ super().__str__()

class matrona_coordinadora(matrona):
        def __str__(self) -> str:
               return 'Matrona Coordinadora '+ super().__str__()

class equipo_medico(models.Model):
        id_equipo = models.IntegerField(primary_key=True)
        numero_serie = models.IntegerField()
        tipos=(('Elige el tipo de equipo','Elige el tipo de equipo'),
                ('Ventilador','Ventilador'),
                ('Incubadora','Incubadora'),
                ('Bomba de infusión', 'Bomba de Infusión'),
                ('Capnógrafo','Capnógrafo'),
                ('EEG','EEG'),
                ('EKG','EKG'),
                ('Saturómetro','Saturómetro'),
                ('Bomba de jeringas','Bomba de jeringas'))
        tipo_equipo = models.TextField(max_length=70, choices=tipos, default='Elige el tipo de equipo')
        descripcion = models.TextField(max_length=250)
        marca = models.TextField(max_length=50)
        condiciones=(('Buen estado','Buen estado'),
                        ('Requiere mantenimiento','Requiere mantenimiento'),
                        ('No utilizable','No utilizable'))
        condicion = models.TextField(max_length=50, choices=condiciones, default='Buen estado')
        estados = (('Disponible','Disponible'),
                   ('En cupo','En cupo'),
                   ('En mantenimiento','En mantenimiento'),
                   ('En préstamo','En préstamo'))
        estado = models.TextField(max_length=50, choices=estados, default='Disponible')
        fecha_mantencion = models.DateField()
        id_matrona = models.ForeignKey(matrona_coordinadora, on_delete=models.CASCADE)

        def __str__(self) -> str:
                return self.tipo_equipo+ ' ' + str(self.id_equipo)

class traslado(models.Model):
        id_traslado = models.IntegerField(primary_key=True)
        razon = models.TextField(max_length=250, blank=True ,null=True)
        fecha_traslado = models.DateField()
        fecha_devolucion = models.DateField()
        id_equipo = models.ForeignKey(equipo_medico, on_delete=models.CASCADE)
        id_matrona = models.ForeignKey(matrona_clinica, on_delete=models.CASCADE)

        def __str__(self) -> str:
               return 'Traslado del equipo '+ str(self.id_equipo)+ ' a mantención con fecha: '+str(self.fecha_traslado)

class prestamo(models.Model):
        id_prestamo = models.IntegerField(primary_key=True)
        fecha_emision = models.DateField()
        fecha_devolucion = models.DateField()
        hospital_destino = models.TextField(max_length=100)
        id_matrona = models.ForeignKey(matrona_clinica, on_delete=models.CASCADE)
        id_equipo = models.ForeignKey(equipo_medico, on_delete=models.CASCADE)

        def __str__(self) -> str:
               return 'Préstamo del equipo '+ str(self.id_equipo) + ' al Hospital '+ self.hospital_destino + ' con fecha '+str(self.fecha_emision)

class cupo(models.Model):
        id_cupo = models.IntegerField(primary_key=True)

        def __str__(self) -> str:
               return 'Cupo '+ str(self.id_cupo)

class equipo_en_cupo(models.Model):
        id_equipo = models.ForeignKey(equipo_medico, on_delete=models.CASCADE, primary_key=True)
        id_cupo = models.ForeignKey(cupo, on_delete=models.CASCADE)
        id_matrona = models.ForeignKey(matrona_clinica, on_delete=models.CASCADE)

        def __str__(self) -> str:
               return 'Equipo '+ str(self.id_equipo) + ' se encuentra en el ' + str(self.id_cupo)

