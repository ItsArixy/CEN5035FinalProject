import connection.py
import mysql.connector

conn = connection.connect_to_database("localhost", "username", "password", "database")
