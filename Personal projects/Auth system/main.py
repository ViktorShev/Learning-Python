from classes import Player, Planet, Universe
from functions import register, verify_credentials

logged_in = False
login_or_register = input('Would you want to login or register? r/l: ')

username = input('Insert your username: ')
password = input('Insert your password: ')

if login_or_register == 'r':
    new_player = register(username, password)
    print(f'Successfully created new player: {new_player.username}')
elif login_or_register == 'l':
    try:
        user_info = verify_credentials(username, password)
        logged_in = user_info[0]
    except (TypeError, NameError) as e:
        print('User does not exist.')
    if logged_in:
        print(f'Successfully logged into: {user_info[1]}')
    else:
        print(f'Incorrect credentials entered for: {user_info[1]}')

if logged_in:
    while True:
        print(f'Current player: {user_info[1]}', f'| Level: {user_info[2]}')
        break