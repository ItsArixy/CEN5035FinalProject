import importlib

#connection to the database
def connect_to_database(host, user, password, database):
    """Connects to the MySQL database."""
    try:
        connector = importlib.import_module("mysql.connector")
        connection = connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        print("Connection to the database was successful.")
        return connection
    except ImportError as err:
        print(f"Error connecting to the database: {err}")
        return None
    except connector.Error as err:
        print(f"Error connecting to the database: {err}")
        return None