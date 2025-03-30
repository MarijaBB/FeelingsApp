import make_connection
from datetime import date, timedelta

today = date.today()

def find_feelings_for_date(userId, date): # want to list feeling(s) for that date
    mydb = make_connection.mydb_connection() 
    mycursor = mydb.cursor()
    sql = """SELECT DISTINCT feelingNAME
            FROM feeldb.feelings f 
                JOIN feeldb.history h on f.feelingId = h.feelingId
                JOIN feeldb.users u on h.userId = u.UserId
            WHERE h.CreatedAt >= %s and h.CreatedAt < %s and u.UserId = %s
           """
    val = (date, date.today() + timedelta(days=1), userId)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()

    list_of_feelings = [f[0] for f in myresult]
    return list_of_feelings

print(find_feelings_for_date(1,today))

def find_dates_for_feeling(userId, feelingId):
    mydb = make_connection.mydb_connection() 
    mycursor = mydb.cursor()
    sql = """SELECT DISTINCT DATE_FORMAT(h.CreatedAt, '%d.%m.%Y.') AS formatted_date
            FROM feeldb.feelings f 
                JOIN feeldb.history h on f.feelingId = h.feelingId
                JOIN feeldb.users u on h.userId = u.UserId
            WHERE h.feelingId = %s and u.UserId = %s
           """
    val = (feelingId, userId)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()

    list_of_dates = [d[0] for d in myresult]
    return list_of_dates

print(find_dates_for_feeling(1,2))
