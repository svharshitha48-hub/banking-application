import mysql.connector
from mysql.connector import Error


def get_connection():
    """
    This function creates and returns a MySQL database connection.
    """

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="nineleaps",
            database="banking_app"
        )

        if connection.is_connected():
            return connection

    except Error as e:
        print("❌ Database connection failed:", e)
        return None