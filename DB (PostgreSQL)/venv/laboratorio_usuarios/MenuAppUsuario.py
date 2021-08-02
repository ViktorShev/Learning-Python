from usuario_dao import UsuarioDAO
from logger_base import log
from usuario import Usuario

while True:
    print('Opciones:\n1) Listar los usuarios.\n2) Agregar un usuario.\n3) Actualizar un usuario.\n4) Eliminar un usuario.\n5) Salir.')
    
    option = input('')
    if option == '1':
        usuarios = UsuarioDAO.select()
        for usuario in usuarios:
            print(usuario)
            
    elif option == '2':
        username = input('Ingrese el username: ')
        password = input('Ingrese el password: ')
        user = Usuario(username=username, password=password)
        UsuarioDAO.insert(user)
        log.info(f'Se inserto el usuario: {user}')
        
    elif option == '3':
        userID = int(input('Ingrese el ID del usuario que quiere modificar: '))
        newUsername = input('Ingrese el nuevo username: ')
        newPassword = input('Ingrese el nuevo password: ')
        user = Usuario(userID, newUsername, newPassword)
        UsuarioDAO.update(user)
        log.info(f'Se actualizo el usuario con ID: {user.id}')
    
    elif option == '4':
        userID = int(input('Ingrese el ID del usuario que desea eliminar: '))
        user = Usuario(id_usuario=userID)
        UsuarioDAO.delete(user)
        log.info(f'Se elimino el usuario con ID: {user.id}')
        
    elif option == '5':
        log.info('Saliendo del programa...')
        break