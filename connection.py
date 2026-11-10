import mysql.connector

#connection to the database
def connect_to_database(host, user, password, database):
    """Connects to the MySQL database."""
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        print("Connection to the database was successful.")
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")
        return None