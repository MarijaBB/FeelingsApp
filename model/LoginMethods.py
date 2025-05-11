from model import make_connection
from datetime import datetime
import bcrypt

def check_if_username_exists(username):
    mydb = make_connection.mydb_connection()
    mycursor = mydb.cursor()
    sql = 'SELECT UserId FROM Users WHERE UserName = %s'
    val = (username,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()
    if myresult == None:
        return None
    return myresult[0]

def check_if_email_exists(email):
    mydb = make_connection.mydb_connection()
    mycursor = mydb.cursor()
    sql = 'SELECT UserId FROM Users WHERE Email = %s'
    val = (email, )
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()
    if myresult == None:
        return None
    return myresult[0]

def check_is_password_correct(email, password):
    mydb = make_connection.mydb_connection()
    mycursor = mydb.cursor()
    sql = 'SELECT PasswordHash,UserId FROM Users WHERE Email = %s'
    val = (email,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()
    if myresult == None:
        return None
    if bcrypt.checkpw(password.encode(), myresult[0].encode()):
        return myresult[1]
    
    return None

def new_user(username, email, password_hash):
    mydb = make_connection.mydb_connection()
    mycursor = mydb.cursor()
    sql = 'INSERT INTO Users (UserName, Email, PasswordHash, CreatedAt) VALUES (%s,%s,%s,%s)'
    val = [(username, email, password_hash, datetime.now())]
    mycursor.executemany(sql, val)
    mydb.commit()
