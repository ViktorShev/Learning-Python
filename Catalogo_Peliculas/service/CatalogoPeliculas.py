import os


class CatalogoPeliculas:
    ruta_archivo = 'peliculas.txt'
    
    @classmethod
    def agregar_pelicula(cls, pelicula):
        with open(cls.ruta_archivo, 'a', encoding='utf8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')
            
    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo, 'r', encoding='utf8') as archivo:
            print('Catalogo de peliculas'.center(50,'-'))
            print('')
            print(archivo.read())
            print('-'*50)
            
    @classmethod
    def eliminar_pelicula(cls):
        with open(cls.ruta_archivo, 'r', encoding='utf8') as archivo:
            peliculas = archivo.readlines()
            
        with open(cls.ruta_archivo,'w', encoding='utf8') as archivo:
            respuesta = input('Ingrese la pelicula que desea eliminar: ')
            for pelicula in peliculas:
                if pelicula.strip('\n') != respuesta:
                    archivo.write(pelicula)
            print(f'Se ha eliminado la pelicula: {respuesta}')
                
    @classmethod
    def eliminar_peliculas(cls):
        os.remove(cls.ruta_archivo)
        print(f'Archivo eliminado: {cls.ruta_archivo}')