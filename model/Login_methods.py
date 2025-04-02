from model import make_connection
from datetime import datetime

def check_if_username_exists(username):
    mydb = make_connection.mydb_connection()
    mycursor = mydb.cursor()
    sql = 'SELECT UserId FROM Users WHERE UserName = %s'
    val = (username,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()
    if myresult == None:
        return -5
    return myresult[0]


def check_if_email_exists(email):
    mydb = make_connection.mydb_connection()
    mycursor = mydb.cursor()
    sql = 'SELECT UserId FROM Users WHERE Email = %s'
    val = (email, )
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()
    if myresult == None:
        return -5
    return myresult[0]

def check_is_password_correct(email, passwordhash):
    mydb = make_connection.mydb_connection()
    mycursor = mydb.cursor()
    sql = 'SELECT UserId FROM Users WHERE Email = %s and PasswordHash = %s'
    val = (email,passwordhash)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()
    if myresult == None:
        return -5
    return myresult[0]

def new_user(username, email, passwordhash):
    mydb = make_connection.mydb_connection()
    mycursor = mydb.cursor()
    sql = 'INSERT INTO Users (UserName, Email, PasswordHash, CreatedAt) VALUES (%s,%s,%s,%s)'
    val = [(username, email, passwordhash, datetime.now())]
    mycursor.executemany(sql, val)
    mydb.commit()


# when log in
def old_user_userId(username, password_hash):
    mydb = make_connection.mydb_connection()
    mycursor = mydb.cursor()
    sql = 'SELECT UserId FROM Users WHERE (UserName = %s or Email = %s) and passwordhash = %s'
    val = (username,username, password_hash)
    mycursor.executemany(sql, val)
    myresult = mycursor.fetchone()
    if myresult[0] > 0:
        return myresult[0]
    return -1