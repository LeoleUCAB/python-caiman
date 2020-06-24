import sqlite3

database = r"./dataBase/pizzaDataBase.db"

# CREATES -------------------------------------------------------------------------------------------------------

sql_create_pizza_table = """ CREATE TABLE IF NOT EXISTS pizza (
                                        primaryKey integer constraint pizza_pk primary key autoincrement,
                                        pizza_id integer not null,
                                        order_fk integer not null,
                                        size_fk integer not null references size,
                                        ingredient_fk integer,
                                        foreign key (ingredient_fk, size_fk) references ingredient
                                    ); """

sql_create_ingredient_table = """ CREATE TABLE IF NOT EXISTS ingredient (
                                        id integer,
                                        size_id integer,
                                        name text not null,
                                        price real not null,
                                        constraint ingredient_pk primary key (id, size_id)
                                    ); """

sql_create_size_table = """ CREATE TABLE IF NOT EXISTS size (
                                    id integer constraint size_pk primary key,
                                    name text,
                                    price real
                                ); """

# INSERTS -------------------------------------------------------------------------------------------------------

sql_insert_pizza_table = """ """
sql_insert_size_table_0 = """INSERT INTO size (id, name, price) VALUES (1, 'Personal', 10)"""
sql_insert_size_table_1 = """INSERT INTO size (id, name, price) VALUES (2, 'Mediana', 15)"""
sql_insert_size_table_2 = """INSERT INTO size (id, name, price) VALUES (3, 'Familiar', 20)"""

sql_insert_ingredient_table_0 = """INSERT INTO ingredient (id, size_id, name, price) VALUES (1, 1, 'Champiñones', 1.75)"""
sql_insert_ingredient_table_1 = """INSERT INTO ingredient (id, size_id, name, price) VALUES (1, 2, 'Champiñones', 2.05)"""
sql_insert_ingredient_table_2 = """INSERT INTO ingredient (id, size_id, name, price) VALUES (1, 3, 'Champiñones', 2.5)"""
sql_insert_ingredient_table_3 = """INSERT INTO ingredient (id, size_id, name, price) VALUES (2, 1, 'Jamón', 1.5)"""
sql_insert_ingredient_table_4 = """INSERT INTO ingredient (id, size_id, name, price) VALUES (2, 2, 'Jamón', 1.75)"""
sql_insert_ingredient_table_5 = """INSERT INTO ingredient (id, size_id, name, price) VALUES (2, 3, 'Jamón', 2)"""

def create_connection(db_file):
    """creating DataBase connection"""

    connection = None
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except:
        print('Ha ocurrido un error en la creacion de la BD')

    return connection

def create_table(connection, create_table_sql, nombreTabla):
    """creating DataBase table"""

    try:
        cursor = connection.cursor()
        cursor.execute(create_table_sql)
        print(f'Creada la tabla: {nombreTabla}')
    except:
        print(f'Ha ocurrido un error al crear la tabla: {nombreTabla}')

def insert_table(connection, insert_table_sql, nombreTabla):

    try:
        cursor = connection.cursor()
        cursor.execute(insert_table_sql)
        print(f'Insertados datos en la tabla: {nombreTabla}')
        connection.commit()
    except:
        print(f'Ha ocurrido un error al insertar los datos en la tabla: {nombreTabla}')


if __name__ == '__main__':
    connection = create_connection(database)

    # create tables
    if connection is not None:
        # create size table
        create_table(connection, sql_create_size_table, "Tamaño")
        # create ingredient table
        create_table(connection, sql_create_ingredient_table, "Ingrediente")
        # create pizza table
        create_table(connection, sql_create_pizza_table, "Pizza")

        #insert in table size
        insert_table(connection, sql_insert_size_table_0, "Tamaño 0")
        insert_table(connection, sql_insert_size_table_1, "Tamaño 1")
        insert_table(connection, sql_insert_size_table_2, "Tamaño 2")

        #insert in table ingrediente
        insert_table(connection, sql_insert_ingredient_table_0, "Ingrediente 0")
        insert_table(connection, sql_insert_ingredient_table_1, "Ingrediente 1")
        insert_table(connection, sql_insert_ingredient_table_2, "Ingrediente 2")
        insert_table(connection, sql_insert_ingredient_table_3, "Ingrediente 3")
        insert_table(connection, sql_insert_ingredient_table_4, "Ingrediente 4")
        insert_table(connection, sql_insert_ingredient_table_5, "Ingrediente 5")
    else:
        print("Error! cannot create the database connection.")