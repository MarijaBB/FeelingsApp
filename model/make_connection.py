import mysql.connector
def mydb_connection():
    try:
        mydb = mysql.connector.connect(
                host="localhost",
                user="",     # not showing publicly
                password="", # not showing publicly
                database = "feelDB"
            )
        return mydb
    except mysql.connector.Error as err:
        print("Error ",err)
        return None