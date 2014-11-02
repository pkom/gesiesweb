#encoding:utf-8

import xml.sax.handler

from django.contrib import admin
from django.contrib.auth.models import User

from .models import Rayuela
from profesores.models import Profesor, CursoProfesor

def import_data(modeladmin, request, queryset):

    class ProfesorHandler(xml.sax.handler.ContentHandler):
        def __init__(self):
            self.buffer = ""
            self.inField = 0

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
                print "Procesando profesor %s %s, %s (%s)" % (self.primerapellido, self.segundoapellido,
                                                                           self.nombre, self.dni)
                print "     es-usuario: %s login: %s id-usuario: %s departamento: %s grupo: %s" % (self.esusuario,
                self.login, self.idusuario, self.departamento, self.grupos)
                # todo: hay que grabar al profesor en profesor, user, etc
                #buscamos en User si ese profesor existe y si no lo damos de alta
                updated_values = {
                    'first_name': self.nombre,
                    'last_name': '%s %s' % (self.segundoapellido, self.primerapellido),
                    'is_staff': True,
                    'is_active': True
                }
                user, created = User.objects.update_or_create(username=self.login, defaults=updated_values)
                profe = user.profesor
                profe.dni = self.dni
                profe.usuario_rayuela = self.login
                profe.es_usuario = self.esusuario
                profe.id_usuario = self.idusuario
                user.profesor = profe
                user.save()
                profe.save()
                #veamos si existe el profesor en el curso
                cursoProfesor = CursoProfesor.objects.all().filter(profesor=profe)
                print cursoProfesor
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


    for rayuela in queryset:
        print 'Procesando archivo',rayuela.archivo
        parser = xml.sax.make_parser()
        handler = ProfesorHandler()
        parser.setContentHandler(handler)
        parser.parse(rayuela.archivo.path)

import_data.short_description = 'Importa datos desde Rayuela'


@admin.register(Rayuela)
class RayuelaAdmin(admin.ModelAdmin):
    list_display = ['curso', 'tipo', 'archivo', 'created', 'procesado']
    readonly_fields = ['procesado', 'resultado']
    ordering = ['-created']
    actions = [import_data]
