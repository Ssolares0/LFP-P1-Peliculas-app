class Peliculas():
    def __init__(self,nombre,actores,año,genero):
        self.nombre = nombre
        self.actores = actores
        self.año = año
        self.genero = genero

    def imprimirPeliculas(self):
        
        print("Pelicula: " + self.nombre +' Actores:' + self.actores +' año: '
        + self.año+ ' Genero: '+ self.genero)
        
        