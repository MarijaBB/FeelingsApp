from model import make_connection 
from datetime import datetime

def insertIntoHistory(feelingId, userId):
    mydb = make_connection.mydb_connection()
    mycursor = mydb.cursor()
    sql = 'INSERT INTO History (UserId, FeelingId, CreatedAt) VALUES (%s,%s,%s)'
    val = [(userId, feelingId, datetime.now())]
    mycursor.executemany(sql, val)

    mydb.commit()
	
def readHistory(userId):
	mydb = make_connection.mydb_connection()

	mycursor = mydb.cursor()
	
	sql = 'SELECT FeelingName, CreatedAt FROM History h JOIN Feelings f on h.FeelingId = f.FeelingId WHERE UserId = %s ORDER BY 2 DESC'
	val = (userId,)
	mycursor.execute(sql, val)
	myresult = mycursor.fetchall()  # List of tuples
	return myresult if myresult else (None,None)

def formatHistory(history):
	history_formatted = []
	for (feeling, time) in history:
		history_formatted.append(time.strftime("%d.%m.%Y %H:%M:%S")+' ** '+feeling+' ** \n')
	return history_formatted