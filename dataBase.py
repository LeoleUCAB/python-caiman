import sqlite3

database = r"./dataBase/pizzaDataBase.db"

sql_create_pizza_table = """ CREATE TABLE IF NOT EXISTS pizza (
                                        id integer PRIMARY KEY,
                                        tamano varchar(30) NOT NULL,
                                        precio double NOT NULL,
                                        check(tamano = "personal" or tamano = "mediana" or tamano = "familiar")
                                    ); """

sql_create_ingrediente_table = """ CREATE TABLE IF NOT EXISTS ingrediente (
                                        id integer PRIMARY KEY,
                                        nombre varchar(30) NOT NULL,
                                        precio double NOT NULL
                                    ); """

sql_create_cliente_table = """ CREATE TABLE IF NOT EXISTS cliente (
                                        id integer PRIMARY KEY,
                                        nombre varchar(30) NOT NULL,
                                        apellido varchar(30) NOT NULL
                                    ); """

sql_create_pedido_table = """ CREATE TABLE IF NOT EXISTS cliente (
                                        id integer PRIMARY KEY,
                                        fecha_pedido date NOT NULL,
                                        precio double NOT NULL,
                                        fk_pizza integer NOT NULL,
                                        fk_cliente integer NOT NULL,
                                        fk_ingrediente integer,
                                        FOREIGN KEY (fk_pizza) REFERENCES pizza (id),
                                        FOREIGN KEY (fk_cliente) REFERENCES cliente (id),
                                        FOREIGN KEY (fk_ingrediente) REFERENCES ingrediente (id)
                                    ); """

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
        print('Ha ocurrido un error al crear la tabla')


if __name__ == '__main__':
    connection = create_connection(database)

    # create tables
    if connection is not None:
        # create pizza table
        create_table(connection, sql_create_pizza_table, "Pizza")

        # create ingrediente table
        create_table(connection, sql_create_ingrediente_table, "Ingrediente")
 
        # create cliente table
        create_table(connection, sql_create_cliente_table, "Cliente")

        # create pedido table
        create_table(connection, sql_create_pedido_table, "Pedido")

    else:
        print("Error! cannot create the database connection.")