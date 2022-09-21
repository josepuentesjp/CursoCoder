from django.shortcuts import render
from django.http import HttpResponse
from App_family.models import family
# Create your views here.

def familia(self):

    father = family(nombre = 'Rolando', years = 2022 - 1958, born_in = '1958-07-05',  hobbie = 'Caminar')
    father.save()
    show = f'El nombre de mi padre es {father.nombre} tiene {father.years} de edad, nació el {father.born_in} y su hobbie es {father.hobbie}.'

    mother = family(nombre = 'Yasmely', years = 2022 - 1965, born_in = '1965-04-05',  hobbie = 'Ir a la iglesia')
    mother.save()
    show2 = f'El nombre de mi madre es {mother.nombre} tiene {mother.years} de edad, nació el {mother.born_in} y su hobbie es {mother.hobbie}.'
    
    sister = family(nombre = 'Rosmely', years = 2022 - 1999, born_in = '1999-08-29',  hobbie = 'Ver series')
    sister.save()
    show3 = f'El nombre de mi hermana es {sister.nombre} tiene {sister.years} de edad, nació el {sister.born_in} y su hobbie es {sister.hobbie}.'

    return HttpResponse(f'{show} <br> {show2} <br> {show3}')
