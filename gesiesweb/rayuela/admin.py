# -*- encoding: utf-8 -*-

import zipfile, os, os.path
import shutil
import xml.sax.handler

from django.utils.safestring import mark_safe
from django.contrib import admin
from django.contrib.auth.models import User
from django.core.files import File

from .models import Rayuela
from profesores.models import Profesor, CursoProfesor
from departamentos.models import Departamento, CursoDepartamento, DepartamentoProfesor
from grupos.models import Grupo, CursoGrupo, GrupoProfesor, GrupoAlumno
from alumnos.models import Alumno, CursoAlumno

def import_data(modeladmin, request, queryset):

    class ProfesorHandler(xml.sax.handler.ContentHandler):

        def __init__(self, request, queryset):
            self.buffer = ""
            self.inField = 0
            self.modeladmin = modeladmin
            self.request = request
            self.queryset = queryset
            self.resultado = u'Proceso de importación iniciado...'

        def get_resultado(self):
            return self.resultado

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
                updated_values = {
                    'first_name': self.nombre,
                    'last_name': '%s %s' % (self.primerapellido, self.segundoapellido),
                    'is_staff': True,
                    'is_active': True
                }
                user, created = User.objects.update_or_create(username=self.login, defaults=updated_values)
                self.resultado += u'Procesando profesor %s' % (user)
                if created:
                    self.resultado += u'Se ha creado el profesor %s' % (user)
                profe = user.profesor
                profe.dni = self.dni
                profe.usuario_rayuela = self.login
                profe.es_usuario = self.esusuario
                profe.id_usuario = self.idusuario
                profe.save()
                #veamos si existe el profesor en el curso
                curso = self.queryset[0].curso
                cursoprofesor, created = CursoProfesor.objects.get_or_create(profesor=profe, curso=curso)
                if created:
                    self.resultado += u'Se ha asignado %s al curso %s' % (profe, curso)
                if self.departamento:
                    departamento, created = Departamento.objects.get_or_create(departamento=self.departamento)
                    if created:
                        self.resultado += u'Se ha creado el departamento %s' % (departamento)
                    cursodepartamento, created = CursoDepartamento.objects.get_or_create(departamento=departamento,
                                                                                         curso=curso)
                    if created:
                        self.resultado += u'Se ha creado el departamento %s en el curso %s' % (departamento, curso)
                    departamentoprofesor, created = DepartamentoProfesor.objects.get_or_create(cursodepartamento=cursodepartamento,
                                                                                               cursoprofesor=cursoprofesor)
                    if created:
                        self.resultado += u'Se ha asignado el profesor %s al departamento %s en el curso %s' %\
                                        (cursoprofesor, cursodepartamento, curso)
                if self.grupos:
                    for grupoit in self.grupos:
                        grupo, created = Grupo.objects.get_or_create(grupo=grupoit)
                        if created:
                            self.resultado += u'Se ha creado el grupo %s' % (grupo)
                        cursogrupo, created = CursoGrupo.objects.get_or_create(grupo=grupo, curso=curso)
                        if created:
                            self.resultado += u'Se ha creado el grupo %s en el curso %s' % (grupo, curso)
                        grupoprofesor, created = GrupoProfesor.objects.get_or_create(cursogrupo=cursogrupo,
                                                                                    cursoprofesor=cursoprofesor)
                        if created:
                            self.resultado += u'Se ha asignado el profesor %s al grupo %s en el curso %s' %\
                                            (cursoprofesor, cursogrupo, curso)
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


    class AlumnoHandler(xml.sax.handler.ContentHandler):

        def __init__(self, request, queryset, dirname):
            self.buffer = ""
            self.inField = 0
            self.modeladmin = modeladmin
            self.request = request
            self.queryset = queryset
            self.rayuela = ''
            self.dirname = dirname
            self.resultado = u'Proceso de importación iniciado...'

        def get_resultado(self):
            return self.resultado

        def startElement(self, name, attrs):
            if name == "nie":
                self.inField = 1
            elif name == "nombre":
                self.inField = 1
            elif name == "primer-apellido":
                self.inField = 1
            elif name == "segundo-apellido":
                self.inField = 1
            elif name == "fecha-nacimiento":
                self.inField = 1
            elif name == "es-usuario":
                self.inField = 1
            elif name == "login":
                self.inField = 1
            elif name == "id-usuario":
                self.inField = 1
            elif name == 'con-foto':
                self.inField = 1
            elif name == 'formato':
                self.inField = 1
            elif name == 'nombre-fichero':
                self.inField = 1
            elif name == "grupo":
                self.inField = 1

        def characters(self, data):
            if self.inField:
                self.buffer += data

        def endElement(self, name):
            if name == "alumno":
                updated_values = {
                    'nombre': self.nombre,
                    'apellidos': '%s %s' % (self.primerapellido, self.segundoapellido),
                    'fecha_nacimiento': self.fechanacimiento,
                    'usuario_rayuela': self.login
                }
                if self.nombrefichero:
                    ficherofoto = os.path.join(self.dirname, 'datos', self.nombrefichero)
                    updated_values['foto'] = File(open(ficherofoto))
                alumno, created = Alumno.objects.update_or_create(nie=self.nie, defaults=updated_values)
                if created:
                    self.resultado += u'Se ha creado el alumno %s' % (alumno)
                alumno.save()
                #veamos si existe el alumno en el curso
                curso = self.queryset[0].curso
                cursoalumno, created = CursoAlumno.objects.get_or_create(alumno=alumno, curso=curso)
                if created:
                    self.resultado += u'Se ha asignado %s al curso %s' % (alumno, curso)
                if self.grupo:
                    grupo, created = Grupo.objects.get_or_create(grupo=self.grupo)
                    if created:
                        self.resultado += u'Se ha creado el grupo %s' % (grupo)
                    cursogrupo, created = CursoGrupo.objects.get_or_create(grupo=grupo, curso=curso)
                    if created:
                        self.resultado += u'Se ha creado el grupo %s en el curso %s' % (grupo, curso)
                    grupoalumno, created = GrupoAlumno.objects.get_or_create(cursogrupo=cursogrupo,
                                                                                cursoalumno=cursoalumno)
                    if created:
                        self.resultado += u'Se ha asignado el alumno %s al grupo %s en el curso %s' %\
                                        (cursoalumno, cursogrupo, curso)
            elif name == "nie":
                self.inField = 0
                self.nie = self.buffer
            elif name == "nombre":
                self.inField = 0
                self.nombre = self.buffer
            elif name == "primer-apellido":
                self.inField = 0
                self.primerapellido = self.buffer
            elif name == "segundo-apellido":
                self.inField = 0
                self.segundoapellido = self.buffer
            elif name == "fecha-nacimiento":
                self.inField = 0
                self.fechanacimiento = self.buffer[-4:]+'-'+self.buffer[3:5]+'-'+self.buffer[0:2]
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
            elif name == "grupo":
                self.inField = 0
                self.grupo = self.buffer
            elif name == 'con-foto':
                self.inField = 0
                if self.buffer == "true":
                    self.confoto = True
                else:
                    self.confoto = False
            elif name == 'formato':
                self.inField = 0
                self.formato = self.buffer
            elif name == 'nombre-fichero':
                self.inField = 0
                self.nombrefichero = self.buffer

            self.buffer = ""
            rayuela = self.rayuela


    for rayuela in queryset:
        parser = xml.sax.make_parser()
        if rayuela.tipo == 'PR':
            handler = ProfesorHandler(request, queryset)
            parser.setContentHandler(handler)
            parser.parse(rayuela.archivo.path)
        elif rayuela.tipo == 'AL':
            dirname = os.path.dirname(rayuela.archivo.path)
            descomprime(rayuela.archivo.path)
            handler = AlumnoHandler(request, queryset, dirname)
            parser.setContentHandler(handler)
            parser.parse(os.path.join(dirname, 'datos', 'Alumnos.xml'))
            try:
                datos = os.path.join(dirname,'datos')
                shutil.rmtree(datos)
            except:
                pass
        rayuela.resultado = handler.get_resultado()
        rayuela.procesado = True
        rayuela.save()

import_data.short_description = 'Importa datos desde Rayuela'

def descomprime(filezip):
    if filezip[-4:].lower() == ".zip":
        # Convert file and dir into absolute paths
        dirname = os.path.dirname(filezip)
        try:
            datos = os.path.join(dirname,'datos')
            shutil.rmtree(datos)
        except:
            pass
        # creamos la nueva carpeta
        try:
            os.mkdir(os.path.join(dirname, 'datos'))
        except:
            pass
        # Get a real Python file handle on the uploaded file
        fullpathhandle = open(filezip, 'r')
        # Unzip the file, creating subdirectories as needed
        zfobj = zipfile.ZipFile(fullpathhandle)
        for name in zfobj.namelist():
            if name.endswith('/'):
                try: # Don't try to create a directory if exists
                    os.mkdir(os.path.join(dirname, name))
                except:
                    pass
            else:
                outfile = open(os.path.join(dirname, 'datos', name), 'wb')
                outfile.write(zfobj.read(name))
                outfile.close()


@admin.register(Rayuela)
class RayuelaAdmin(admin.ModelAdmin):
    list_display = ['curso', 'tipo', 'archivo', 'created', 'modified', 'procesado']
    readonly_fields = ['procesado', 'resultado']
    ordering = ['-created']
    actions = [import_data]
