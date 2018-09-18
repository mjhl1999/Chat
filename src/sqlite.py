import sqlite

#creando base de datos en RAM
db = sqlite3.connect(':memory:')
db = sqlite3.connect('data/mydb')

# Get un objeto cursor
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE users(nombre TEXT, estado TEXT, conexion TEXT)
''')
db.commit()
