from django.forms import ModelForm
from django import forms
from .models import equipo_medico, traslado, prestamo, matrona_coordinadora,matrona_clinica

FORMATOS_FECHA = ('%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y', '%m/%d/%Y', '%d/%m/%y', '%d/%m/%Y')

class nuevoEquipoForm(ModelForm):
    id_equipo = forms.IntegerField()
    numero_serie = forms.IntegerField()
    tipos=(('Elige el tipo de equipo','Elige el tipo de equipo'),
                ('Ventilador','Ventilador'),
                ('Incubadora','Incubadora'),
                ('Bomba de infusión', 'Bomba de Infusión'),
                ('Capnógrafo','Capnógrafo'),
                ('EEG','EEG'),
                ('EKG','EKG'),
                ('Saturómetro','Saturómetro'),
                ('Bomba de jeringas','Bomba de jeringas'))
    tipo_equipo = forms.ChoiceField(choices=tipos)
    descripcion = forms.CharField()
    marca = forms.CharField()
    condiciones=(('Buen estado','Buen estado'),
                        ('Requiere mantenimiento','Requiere mantenimiento'),
                        ('No utilizable','No utilizable'))
    condicion = forms.ChoiceField(choices=condiciones)
    estados = (('Disponible','Disponible'),
                   ('En cupo','En cupo'),
                   ('En mantenimiento','En mantenimiento'),
                   ('En préstamo','En préstamo'))
    estado = forms.ChoiceField(choices=estados)
    fecha_mantencion = forms.DateField(input_formats=FORMATOS_FECHA)


    class Meta:
        model = equipo_medico
        exclude = ['user']
    


class nuevoTrasladoForm(ModelForm):
    id_traslado = forms.IntegerField()
    razon = forms.CharField()
    fecha_traslado = forms.DateField(input_formats=FORMATOS_FECHA)
    fecha_devolucion = forms.DateField(input_formats=FORMATOS_FECHA)

    class Meta:
        model = traslado
        exclude = ['user']

class nuevoPrestamoForm(ModelForm):
    id_prestamo = forms.IntegerField()
    fecha_emision = forms.DateField(input_formats=FORMATOS_FECHA)
    fecha_devolucion = forms.DateField(input_formats=FORMATOS_FECHA)
    hospital_destino = forms.CharField()

    class Meta:
        model = prestamo
        exclude = ['user']
