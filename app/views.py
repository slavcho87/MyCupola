from django.shortcuts import render
import json
from Fachada import Fachada
from django.http import HttpResponse
# Create your views here.

class AtenderPeticiones(object):
    """docstring for AtenderPeticiones"""
    def __init__(self, arg):
        self.arg = arg
    
    @staticmethod
    def register(request):
        email = request.GET.get('email', 'error')
        password = request.GET.get('password', 'error')

        if email=='error' or password == 'error':
            return HttpResponse(json.dumps({'registrado' : 'false'}))
        else:
            fachada = Fachada()
            registrado = fachada.registrarUsuario(email, password)
            if registrado:
                request.session['email'] = email
                request.session['logged'] = 'true'
                return HttpResponse(json.dumps({'registrado' : 'true'}))
            else:
                return HttpResponse(json.dumps({'registrado' : 'false'}))

    @staticmethod
    def login (request):
        email = request.GET.get('email', 'error')
        password = request.GET.get('password', 'error')
        #return HttpResponse(json.dumps({'login' : 'false'}))
        if email=='error' or password == 'error':
        #if True:
            return HttpResponse(json.dumps({'login' : 'false'}))
        else:
            fachada = Fachada()
            logeado = fachada.login(email, password)
            if logeado:
                request.session['email'] = email
                return HttpResponse(json.dumps({'login' : 'true'}))
            else:
                return HttpResponse(json.dumps({'login' : 'false'}))

    @staticmethod
    def crearAlbum (request):
        email = request.session['email']
        if not email:
            return json.dumps({'crear' :'error',
                'descripcion':'no se encuentra email'})
        nombre_album = request.get('nombre_album')
        fachada = Fachada()
        creado = fachada.crearAlbum(email, nombre_album)
        if creado:
            return HttpResponse(json.dumps({'crear' : 'ok'}))
        else:
            return HttpResponse(json.dumps({'crear' :'error',
                'descripcion':'error con base de datos'}))

    @staticmethod
    def meGustaImagen(request):
        email = request.session['email']
        if not email:
            return json.dumps({'votar' :'error',
                'descripcion':'no se encuentra email'})
        fachada = Fachada()
        votado = fachada.meGustaImagen(email)
        if votado:
            return HttpResponse(json.dumps({'votar' :'ok',
                'descripcion':'votado correctamente'}))
        else:
            return HttpResponse(json.dumps({'votar ' :'error',
                'descripcion':'error con base de datos'}))

    @staticmethod
    def getImagen(request):
        email = request.session['email']
        if not email:
            return HttpResponse(json.dumps({'getImagen' :'error',
                'descripcion':'no estas logeado'}))

        zoom = request.get('val0', 'error')
        coord1 = request.get('val1','error')
        coord2 = request.get('val2','error')

        if zoom == 'error' or coord1 == 'error' or coord2 == 'error':
            return HttpResponse(son.dumps({'getImagen' :'error',
                'descripcion':'no estas logeado'}))
        else:
            #llamar a lo de suavi.
            return None

    @staticmethod
    def index(request):
        return render(request, 'app/tests/opacity.html')
    