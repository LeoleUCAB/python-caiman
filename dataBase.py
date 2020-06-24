import sqlite3

database = r"./dataBase/pizzaDataBase.db"

# CREATES -------------------------------------------------------------------------------------------------------

sql_create_pizza_table = """ CREATE TABLE IF NOT EXISTS pizza (
                                        primaryKey integer constraint pizza_pk primary key autoincrement,
                                        pizza_id integer not null,
                                        order_fk integer not null,
                                        size_fk integer not null references size,
                                        ingredient_fk integer not null,
                                        pedido_fk integer not null,
                                        foreign key (ingredient_fk, size_fk) references ingredient,
                                        foreign key (pedido_fk) references pedido
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

sql_create_pedido_table = """ CREATE TABLE IF NOT EXISTS pedido (
                                    id integer constraint pedido_pk primary key,
                                    fecha date not null
                                ); """

# INSERTS -------------------------------------------------------------------------------------------------------

sql_insert_size_table_personal = """INSERT INTO size (id, name, price) VALUES (1, 'Personal', 10)"""
sql_insert_size_table_mediana = """INSERT INTO size (id, name, price) VALUES (2, 'Mediana', 15)"""
sql_insert_size_table_familiar = """INSERT INTO size (id, name, price) VALUES (3, 'Familiar', 20)"""

sql_insert_ingredient_table_jamonPersonal = """INSERT INTO ingredient (id, size_id, name, price) VALUES (1, 1, 'Jamón', 1.5)"""
sql_insert_ingredient_table_jamonMediano = """INSERT INTO ingredient (id, size_id, name, price) VALUES (1, 2, 'Jamón', 1.75)"""
sql_insert_ingredient_table_jamonFamiliar = """INSERT INTO ingredient (id, size_id, name, price) VALUES (1, 3, 'Jamón', 2)"""

sql_insert_ingredient_table_champinonPersonal = """INSERT INTO ingredient (id, size_id, name, price) VALUES (2, 1, 'Champiñones', 1.75)"""
sql_insert_ingredient_table_champinonMediano = """INSERT INTO ingredient (id, size_id, name, price) VALUES (2, 2, 'Champiñones', 2.05)"""
sql_insert_ingredient_table_champinonFamiliar = """INSERT INTO ingredient (id, size_id, name, price) VALUES (2, 3, 'Champiñones', 2.5)"""

sql_insert_ingredient_table_pimentonPersonal = """INSERT INTO ingredient (id, size_id, name, price) VALUES (3, 1, 'Pimentón', 1.5)"""
sql_insert_ingredient_table_pimentonMediano = """INSERT INTO ingredient (id, size_id, name, price) VALUES (3, 2, 'Pimentón', 1.75)"""
sql_insert_ingredient_table_pimentonFamiliar = """INSERT INTO ingredient (id, size_id, name, price) VALUES (3, 3, 'Pimentón', 2)"""

sql_insert_ingredient_table_dobleQuesoPersonal = """INSERT INTO ingredient (id, size_id, name, price) VALUES (4, 1, 'Doble Queso', 0.8)"""
sql_insert_ingredient_table_dobleQuesoMediano = """INSERT INTO ingredient (id, size_id, name, price) VALUES (4, 2, 'Doble Queso', 1.3)"""
sql_insert_ingredient_table_dobleQuesoFamiliar = """INSERT INTO ingredient (id, size_id, name, price) VALUES (4, 3, 'Doble Queso', 1.7)"""

sql_insert_ingredient_table_AceitunaPersonal = """INSERT INTO ingredient (id, size_id, name, price) VALUES (5, 1, 'Aceituna', 1.8)"""
sql_insert_ingredient_table_AceitunaMediano = """INSERT INTO ingredient (id, size_id, name, price) VALUES (5, 2, 'Aceituna', 2.15)"""
sql_insert_ingredient_table_AceitunaFamiliar = """INSERT INTO ingredient (id, size_id, name, price) VALUES (5, 3, 'Aceituna', 2.6)"""

sql_insert_ingredient_table_pepperoniPersonal = """INSERT INTO ingredient (id, size_id, name, price) VALUES (6, 1, 'Pepperoni', 1.25)"""
sql_insert_ingredient_table_pepperoniMediano = """INSERT INTO ingredient (id, size_id, name, price) VALUES (6, 2, 'Pepperoni', 1.7)"""
sql_insert_ingredient_table_pepperoniFamiliar = """INSERT INTO ingredient (id, size_id, name, price) VALUES (6, 3, 'Pepperoni', 1.9)"""

sql_insert_ingredient_table_salchichonPersonal = """INSERT INTO ingredient (id, size_id, name, price) VALUES (7, 1, 'Salchichón', 1.6)"""
sql_insert_ingredient_table_salchichonMediano = """INSERT INTO ingredient (id, size_id, name, price) VALUES (7, 2, 'Salchichón', 1.85)"""
sql_insert_ingredient_table_salchichonFamiliar = """INSERT INTO ingredient (id, size_id, name, price) VALUES (7, 3, 'Salchichón', 2.1)"""

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
        # create pedido table
        create_table(connection, sql_create_pedido_table, "Pedido")
        # create pizza table
        create_table(connection, sql_create_pizza_table, "Pizza")

        #insert in table size
        insert_table(connection, sql_insert_size_table_personal, "Tamaño personal")
        insert_table(connection, sql_insert_size_table_mediana, "Tamaño mediano")
        insert_table(connection, sql_insert_size_table_familiar, "Tamaño familiar")

        #insert in table ingrediente
        insert_table(connection, sql_insert_ingredient_table_jamonPersonal, "Jamón personal")
        insert_table(connection, sql_insert_ingredient_table_jamonMediano, "Jamón mediano")
        insert_table(connection, sql_insert_ingredient_table_jamonFamiliar, "Jamón familiar")

        insert_table(connection, sql_insert_ingredient_table_champinonPersonal, "Champiñon personal")
        insert_table(connection, sql_insert_ingredient_table_champinonMediano, "Champiñon mediano")
        insert_table(connection, sql_insert_ingredient_table_champinonFamiliar, "Champiñon familiar")

        insert_table(connection, sql_insert_ingredient_table_pimentonPersonal, "Pimentón personal")
        insert_table(connection, sql_insert_ingredient_table_pimentonMediano, "Pimentón mediano")
        insert_table(connection, sql_insert_ingredient_table_pimentonFamiliar, "Pimentón familiar")

        insert_table(connection, sql_insert_ingredient_table_dobleQuesoPersonal, "Doble Queso personal")
        insert_table(connection, sql_insert_ingredient_table_dobleQuesoMediano, "Doble Queso mediano")
        insert_table(connection, sql_insert_ingredient_table_dobleQuesoFamiliar, "Doble Queso familiar")

        insert_table(connection, sql_insert_ingredient_table_AceitunaPersonal, "Aceituna personal")
        insert_table(connection, sql_insert_ingredient_table_AceitunaMediano, "Aceituna mediana")
        insert_table(connection, sql_insert_ingredient_table_AceitunaFamiliar, "Aceituna familiar")

        insert_table(connection, sql_insert_ingredient_table_pepperoniPersonal, "Pepperoni personal")
        insert_table(connection, sql_insert_ingredient_table_pepperoniMediano, "Pepperoni mediano")
        insert_table(connection, sql_insert_ingredient_table_pepperoniFamiliar, "Pepperoni familiar")

        insert_table(connection, sql_insert_ingredient_table_salchichonPersonal, "Salchichon personal")
        insert_table(connection, sql_insert_ingredient_table_salchichonMediano, "Salchichon mediano")
        insert_table(connection, sql_insert_ingredient_table_salchichonFamiliar, "Salchichon familiar")
    else:
        print("Error! cannot create the database connection.")