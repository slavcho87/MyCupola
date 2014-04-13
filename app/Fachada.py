from app.models import *

class Fachada(object):
    """ Interacciona con la base de datos."""

    
    def registrarUsuario(self, email, password ):
        return True
        # si todo va bien return true, else false..

    def login(self, email, password):
        return True

    
    def crearAlbum(self, nombre_album):
        return True


    def meGustaImagen(self, url_foto):
        return True

    def guardarPartida(self):
        return True

    def getImagen(self, zoom, coord1, coord2):
        return True
        