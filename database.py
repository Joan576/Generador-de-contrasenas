import sqlite3

def conectar_bd():
    #Funcion para conectar la base de datos SQLite
    conn = sqlite3.connect('contraseñas.db')
    return conn

def crear_tabla():
    #Funcion para crear la tabla de contraseñas
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contraseñas (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   contraseña TEXT NO NULL 
                   
                )
    ''')
    conn.commit()
    conn.close()

def guardar_contraseña(contraseña):
    #Funcion para guardar la contraseña en la base de datos.
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO contraseñas (contraseña) VALUES (?)', (contraseña,))
    conn.commit()
    conn.close()


