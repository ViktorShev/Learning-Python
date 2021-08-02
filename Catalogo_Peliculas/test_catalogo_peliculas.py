from domain.Pelicula import Pelicula
from service.CatalogoPeliculas import CatalogoPeliculas

while True:
    print(f'\nSeleccione una opcion:\n1) Agregar una pelicula\n2) Listar las peliculas\n3) Eliminar una pelicula del catalogo\n4) Eliminar el catalogo de peliculas\n5) Salir')
    print('')
    respuesta = input('')
    if respuesta == '1':
        nombre_pelicula = input('Ingrese el nombre de la pelicula: ')
        pelicula = Pelicula(nombre_pelicula)
        CatalogoPeliculas.agregar_pelicula(pelicula)
        print(f'Se ha añadido la pelicula: {nombre_pelicula}.')
    elif respuesta == '2':
        try:
            CatalogoPeliculas.listar_peliculas()
        except FileNotFoundError as e:
            print(f'\nEl catalogo de peliculas ha sido eliminado o no existe.')
    elif respuesta == '3':
        CatalogoPeliculas.eliminar_pelicula()
    elif respuesta == '4':
        try:
            CatalogoPeliculas.eliminar_peliculas()
        except FileNotFoundError as e:
            print(f'\nEl catalogo ya ha sido eliminado o no existe.')
    elif respuesta == '5':
        print('Saliendo del programa...')
        break