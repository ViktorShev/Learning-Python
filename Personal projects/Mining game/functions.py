import keyboard
import hashlib
from classes import Player
from db_connection import Connection
from random import randint

salt_dict = {
    1: 'thisisasecret',
    2: 'testsalt',
    3: 'definitelysafe',
    4: 'saltysalt',
    5: 'normalsalt'
}


def hasher(password, salt_id=None):
    salt = salt_dict[salt_id].encode('utf-8')
    password = password.encode('utf-8')
    new_password = hashlib.pbkdf2_hmac('md5', password, salt, 1, None).hex()
    return new_password
        
def register(username, password):
    salt_id = randint(1,5)
    conn = Connection.getConnection()
    new_password = hasher(password, salt_id)
    new_player = Player(username, new_password)
    user_info = new_player._CREDENTIALS["username"], new_player._CREDENTIALS["password"], 0, salt_id
    with conn:
        with conn.cursor() as cur:
            SQL = "INSERT INTO users (username, password, level, salt) VALUES (%s, %s, %s, %s)"
            cur.execute(SQL, user_info)
    Connection.freeConn(conn)
    
    return new_player

def verify_credentials(username, password):
    conn = Connection.getConnection()
    with conn:
        with conn.cursor() as cur:
            SQL = 'SELECT * FROM users WHERE username = %s'
            cur.execute(SQL, (username,))
            user_info = cur.fetchone()
            salt_id = user_info[4]
            hash = hasher(password, salt_id)
    Connection.freeConn(conn)
    if user_info[2] != hash:
        return False, user_info[1]
    elif user_info[2] == hash:
        return True, user_info[1]
