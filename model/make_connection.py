import mysql.connector
def mydb_connection():
    return mysql.connector.connect(
            host="localhost",
            user="",     # not showing publicly
            password="", # not showing publicly
            database = "feelDB"
        )