import sqlite3

def create_connection(db_file):
    """creating DataBase connection"""

    connection = None
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except:
        print('Ha ocurrido un error en la creacion de la BD')

    return connection

def create_table(connection, create_table_sql):
    """creating DataBase table"""

    try:
        cursor = connection.cursor()
        cursor.execute(create_table_sql)
    except:
        print('Ha ocurrido un error al crear la tabla')