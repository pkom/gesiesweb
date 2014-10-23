========================
Proyecto GesIESWeb
========================

Proyecto ideado para llevar el control disciplinario, retrasos, absentismos pasivos, evaluaciones y fichas de tutores
en los centros de educación secundaria de Extremadura.

Los datos son importados al sistema desde los archivos generados por la plataforma Rayuela del Gobierno de Extremadura.

Está realizado en Django 1.6.

Para utilizarlo:

#. Crea un entorno virtual de desarrollo para python, con virtualenv y lo activas
#. Instala Django 1.6.7
#. Clona este repositorio desde github con git clone git@github.com:pkom/gesiesweb.git
#. Instala las dependencias con pip install -r requirements/local.txt
#. Configura los valores apropiados en el archivo settings.json según tu base de datos y demás
#. Sincroniza la base de datos con python manage.py syncdb
#. Corre el servidor con python manage.py runserver

