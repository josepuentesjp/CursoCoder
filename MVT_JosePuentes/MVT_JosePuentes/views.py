from multiprocessing import context
from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime as dt
from datetime import date

def about(request):
    return HttpResponse("<center><h1>Mi nombre es José Puentes, y este es mi primer MVT</h1></center>")

def bienvenida(self):

    fecha_y_hora = dt.now()

    miHtml = loader.get_template('Template1.html')

    miContexto = {'dia': fecha_y_hora}

    documento = miHtml.render(miContexto)

    return HttpResponse(documento)

