from django.shortcuts import render
import json
from fachada import Fachada
# Create your views here.

class AtenderPeticiones(object):
    """docstring for AtenderPeticiones"""
    def __init__(self, arg):
        self.arg = arg
        
    def register(self, request):
        email = request.get('email', 'error')
        password = request.get('password', 'error')

        if email=='error' or password == 'error':
            return json.dumps({'registrado' : 'false'})
        else:
            fachada = Fachada()
            registrado = fachada.registrarUsuario(email, password)
            if registrado:
                request.session['email'] = email
                request.session['logged'] = 'true'
                return json.dumps({'registrado' : 'true'})
            else:
                return json.dumps({'registrado' : 'false'})

    def login (self, request):
        email = request.get('email', 'error')
        password = request.get('password', 'error')

        if email=='error' or password == 'error':
            return json.dumps({'login' : 'false'})
        else:
            fachada = Fachada()
            logeado = fachada.login(email, password)
            if logeado:
                request.session['email'] = email
                request.session['logged'] = 'true'
                return json.dumps({'login' : 'true'})
            else:
                return json.dumps({'login' : 'false'})


    def crearAlbum (self, request):
        email = request.session['email']
        if not email:
            return json.dumps({'crear' :'error',
                'descripcion':'no se encuentra email'})
        nombre_album = request.get('nombre_album')
        fachada = Fachada()
        creado = fachada.crearAlbum(nombre_album)
        if creado:
            return json.dumps({'crear' : 'ok'})
        else:
            return json.dumps({'crear' :'error',
                'descripcion':'error con base de datos'})

    def meGustaImagen(self, request):
        email = request.session['email']
        if not email:
            return json.dumps({'votar' :'error',
                'descripcion':'no se encuentra email'})
        fachada = Fachada()
        votado = fachada.meGustaImagen()
        if votado:
            return json.dumps({'votar' :'ok',
                'descripcion':'votado correctamente'})
        else:
            return json.dumps({'votar ' :'error',
                'descripcion':'error con base de datos'})

    def getImagen(self, request):
        email = request.session['email']
        if not email:
            return json.dumps({'getImagen' :'error',
                'descripcion':'no estas logeado'})

        zoom = request.get('val0', 'error')
        coord1 = request.get('val1','error')
        coord2 = request.get('val2','error')

        if zoom == 'error' or coord1 == 'error' or coord2 == 'error':
            return json.dumps({'getImagen' :'error',
                'descripcion':'no estas logeado'})
        else:
            #llamar a lo de suavi.
            return None

    