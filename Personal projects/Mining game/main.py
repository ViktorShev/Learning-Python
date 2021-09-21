from classes import Player, Planet, Universe
from functions import register, log_in

logged_in = False
login_or_register = input('Would you want to login or register? r/l: ')

username = input('Insert your username: ')
password = input('Insert your password: ')

if login_or_register == 'r':
    player = register(username, password)
    print(f'Created new player: {player.username}')
elif login_or_register == 'l':
    logged_in = log_in(username, password)
    if logged_in:
        print('Successfully logged in.')