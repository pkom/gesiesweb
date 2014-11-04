#encoding:utf-8

import xml.sax.handler

from django.contrib import admin
from django.contrib.auth.models import User

from .models import Rayuela
from profesores.models import Profesor, CursoProfesor

def import_data(modeladmin, request, queryset):

    class ProfesorHandler(xml.sax.handler.ContentHandler):
        def __init__(self, rayuela, request, queryset):
            self.buffer = ""
            self.inField = 0
            self.modeladmin = modeladmin
            self.request = request
            self.queryset = queryset
            self.rayuela = ''

        def startElement(self, name, attrs):
            if name == "dni":
                self.inField = 1
            elif name == "nombre":
                self.inField = 1
            elif name == "primer-apellido":
                self.inField = 1
            elif name == "segundo-apellido":
                self.inField = 1
            elif name == "es-usuario":
                self.inField = 1
            elif name == "login":
                self.inField = 1
            elif name == "id-usuario":
                self.inField = 1
            elif name == "departamento":
                self.inField = 1
            elif name == "grupos":
                self.grupos = []
            elif name == "grupo":
                self.inField = 1

        def characters(self, data):
            if self.inField:
                self.buffer += data

        def endElement(self, name):
            if name == "profesor":
                self.rayuela += u"Procesando profesor %s %s, %s (%s)" % (self.primerapellido, self.segundoapellido,
                                                                           self.nombre, self.dni)
                updated_values = {
                    'first_name': self.nombre,
                    'last_name': '%s %s' % (self.primerapellido, self.segundoapellido),
                    'is_staff': True,
                    'is_active': True
                }
                user, created = User.objects.update_or_create(username=self.login, defaults=updated_values)
                profe = user.profesor
                profe.dni = self.dni
                profe.usuario_rayuela = self.login
                profe.es_usuario = self.esusuario
                profe.id_usuario = self.idusuario
                profe.save()
                #veamos si existe el profesor en el curso
                curso = self.queryset[0].curso
                cursoprofesor = CursoProfesor.objects.get_or_create(profesor=profe, curso=curso)
            elif name == "dni":
                self.inField = 0
                self.dni = self.buffer
            elif name == "nombre":
                self.inField = 0
                self.nombre = self.buffer
            elif name == "primer-apellido":
                self.inField = 0
                self.primerapellido = self.buffer
            elif name == "segundo-apellido":
                self.inField = 0
                self.segundoapellido = self.buffer
            elif name == "es-usuario":
                self.inField = 0
                if self.buffer == "true":
                    self.esusuario = True
                else:
                    self.esusuario = False
            elif name == "login":
                self.inField = 0
                self.login = self.buffer
            elif name == "id-usuario":
                self.inField = 0
                self.idusuario = self.buffer
            elif name == "departamento":
                self.inField = 0
                self.departamento = self.buffer
            elif name == "grupo":
                self.inField = 0
                self.grupo = self.buffer
                self.grupos.append(self.grupo)

            self.buffer = ""
            rayuela = self.rayuela


    for rayuela in queryset:
        rayuela.resultado = u'Proceso de importación iniciado...'
        parser = xml.sax.make_parser()
        handler = ProfesorHandler(rayuela.resultado, request, queryset)
        parser.setContentHandler(handler)
        parser.parse(rayuela.archivo.path)
        rayuela.resultado += u'Proceso finalizado...'
        rayuela.procesado = True
        rayuela.save()

import_data.short_description = 'Importa datos desde Rayuela'


@admin.register(Rayuela)
class RayuelaAdmin(admin.ModelAdmin):
    list_display = ['curso', 'tipo', 'archivo', 'created', 'modified', 'procesado']
    readonly_fields = ['procesado', 'resultado']
    ordering = ['-created']
    actions = [import_data]
