from app.models import *
import random

class Fachada(object):
    """ Interacciona con la base de datos."""
	
    def registrarUsuario(self, email, password ):
        """ Devuelve true si y solo si el usuario ha sido registrado."""
            usuario = Usuario.objects.filter(email=registroEmail)
            if not usuario:
                nuevoUsuario = Usuario()
                nuevoUsuario.email = email
                nuevoUsuario.password = password
                nuevoUsuario.save()
	        return True
            else:
                return False
 
    def login(self, email, password):
        """ Devuelve true si y solo si el usuario esta registrado"""
        usuario = Usuario.objects.filter(email=email,password=password)
        if not usuario:
            return False
        else: 
            return True	

	def crearAlbum(self, email, nombre_album):
        """ Devuelve true si y solo si el album nombre_album ha sido creado"""
            usuario = Usuario.objects.filter(email=email)
            if not usuario:
                return False
            else:
               usuario.albumes_set.create(nombre = nombre_album)
               return True

	def meGustaImagen(self, email, url_imagen):
            usuario = Usuario.objects.filter(email=email)
            imagen = Imagen.objects.filter(direccion=url_imagen)
            if not usuario or not imagen:
                return False
            else:
                meGusta = MeGusta()
                meGusta.usuario_set.add(usuario)
                meGusta.imagen_set.add(imagen)
                meGusta.save() 
 
    def guardarPartida(self):
        return True
                
            
