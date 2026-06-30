import sqlite3

conexao = sqlite3.connect("usuarios.db")
cursor = conexao.cursor()

cursor.execute(
"""CREATE TABLE IF NOT EXISTS usuarios(
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 usuario TEXT UNIQUE, 
 senha TEXT
)"""
)

conexao.commit()

