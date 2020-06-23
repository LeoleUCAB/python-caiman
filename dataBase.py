import sqlite3

database = r"./dataBase/pizzaDataBase.db"

sql_create_pizza_table = """ CREATE TABLE IF NOT EXISTS pizza (
                                        primaryKey integer constraint pizza_pk primary key autoincrement,
                                        pizza_id integer not null,
                                        order_fk integer not null,
                                        size_fk integer not null references size,
                                        ingredient_fk integer,
                                        foreign key (ingredient_fk, size_fk) references ingredient
                                    ); """

sql_create_ingrediente_table = """ CREATE TABLE IF NOT EXISTS ingrediente (
                                        id integer,
                                        size_id integer,
                                        name text not null,
                                        price   real not null,
                                        constraint ingredient_pk primary key (id, size_id)
                                    ); """

sql_create_size_table = """ CREATE TABLE IF NOT EXISTS size (
                                    id integer constraint size_pk primary key,
                                    name text,
                                    price real
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
        print(f'Ha ocurrido un error al crear la tabla: {nombreTabla}')


if __name__ == '__main__':
    connection = create_connection(database)

    # create tables
    if connection is not None:
        # create pizza table
        create_table(connection, sql_create_pizza_table, "Pizza")

        # create ingrediente table
        create_table(connection, sql_create_ingrediente_table, "Ingrediente")
 
        # create size table
        create_table(connection, sql_create_size_table, "Tamaño")

    else:
        print("Error! cannot create the database connection.")