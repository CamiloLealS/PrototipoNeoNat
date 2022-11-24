from django.contrib import admin
from .models import equipo_medico, matrona, matrona_clinica, matrona_coordinadora, equipo_en_cupo, cupo, traslado, prestamo 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
admin.site.register(equipo_medico)
admin.site.register(matrona)
admin.site.register(matrona_coordinadora)
admin.site.register(matrona_clinica)
admin.site.register(equipo_en_cupo)
admin.site.register(cupo)
admin.site.register(traslado)
admin.site.register(prestamo)