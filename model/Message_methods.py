import random
from model import make_connection 
def findMessageforFeeling(feelingId):
    mydb = make_connection.mydb_connection()
    mycursor = mydb.cursor()

    sql = 'SELECT message, ColorCode FROM Messages m join Feelings f on m.FeelingId = f.FeelingId WHERE m.FeelingId = %s'
    val = (feelingId,)
    mycursor.execute(sql, val)

    myresult = mycursor.fetchall() 
    if len(myresult) == 0:
        return None, None 

    i = random.randint(0,len(myresult)-1)
    message = myresult[i][0]
    color = myresult[i][1]
    
    return (message,color) 
