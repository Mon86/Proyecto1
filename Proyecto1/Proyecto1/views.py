from django.http import HttpResponse
from django.template import Template,Context
import datetime

def saludo(request):
	return HttpResponse ( " Hola Chicos")

def diaDeHoy(request):
	dia = datetime.datetime.now()
	documentoDeTexto = f"Hoy es dia <br> {dia}"
	return HttpResponse (  documentoDeTexto)

def segunda_vista(request):
	return HttpResponse ( " <br><br><br><br>Hola Chicos")

def miNombre (sefl,nombre):
	documentoDeTexto = f"miNombre es: <br><br>  <h1> {nombre}<h1>"
	return HttpResponse(documentoDeTexto)

def template(self):
	miHtml = open ("C:/Users/hugom/Downloads/Proyecto1/Proyecto1/Proyecto1/plantillas/template.html")
	plantilla= Template(miHtml.read())
	miHtml.close()
	miContext= Context()
	documento = plantilla.render(miContext)
	return HttpResponse(documento) 