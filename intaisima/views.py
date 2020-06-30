from django.http import HttpResponse #importa utileria de http
from datetime import datetime

def hola_mundo(request):
	now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs ')
	print (now)
	return HttpResponse("Hello, World: La hora del servidor es {now}".format(now=str(now)) )
#funcion obtener usuario y edad
def say_hi(request, name, age):
	if age <13:
		mensaje = "Lo siento! {} no puedes acceder aquí".format(name)
	else:
		mensaje = "Bienvenido {}".format(name)
	return HttpResponse(mensaje)