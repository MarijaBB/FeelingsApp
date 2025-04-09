from model import make_connection

def getImage(feelingId):
    mydb = make_connection.mydb_connection() 
    mycursor = mydb.cursor()
    sql = 'SELECT Image FROM Feelings WHERE FeelingId=%s'
    val = (feelingId,)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchone()
    return myresult[0].strip()

def getFeelingName(feelingId):
    mydb = make_connection.mydb_connection()  
    mycursor = mydb.cursor()
    sql = 'SELECT FeelingName FROM Feelings WHERE FeelingId=%s'
    val = (feelingId,)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchone()
    return myresult[0].strip()

def getFeelings():
    mydb = make_connection.mydb_connection()  
    mycursor = mydb.cursor()
    sql = 'SELECT FeelingName FROM Feelings'
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return [f[0] for f in myresult]
