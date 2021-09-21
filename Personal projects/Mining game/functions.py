import keyboard
import hashlib
from classes import Player
from db_connection import Connection


def hasher(password):
    new_password = hashlib.md5(password.encode()).hexdigest()

    return new_password
        
def register(username, password):
    conn = Connection.getConnection()
    new_password = hasher(password)
    new_player = Player(username, new_password)
    user_info = new_player._CREDENTIALS["username"], new_player._CREDENTIALS["password"], 0
    with conn:
        with conn.cursor() as cur:
            SQL = "INSERT INTO users (username, password, level) VALUES (%s, %s, %s)"
            cur.execute(SQL, user_info)
    Connection.freeConn(conn)
    
    return new_player

def log_in(username, password):
    conn = Connection.getConnection()
    hash = hasher(password)
    with conn:
        with conn.cursor() as cur:
            SQL = 'SELECT * FROM users WHERE username = %s'
            cur.execute(SQL, (username,))
            credentials = cur.fetchone()
    Connection.freeConn(conn)
    if credentials[2] != hash:
        return False
    elif credentials[2] == hash:
        return True
