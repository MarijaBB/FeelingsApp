from model import make_connection
from datetime import date,datetime, timedelta

today = date.today()

def find_feelings_for_dates(userId, dateFrom, dateTo): # want to list feeling(s) for that date
    mydb = make_connection.mydb_connection() 
    mycursor = mydb.cursor()
    from_date = datetime.strptime(dateFrom, "%d/%m/%Y").strftime("%Y-%m-%d")
    to_date_plus_one = (datetime.strptime(dateTo, "%d/%m/%Y") + timedelta(days=1)).strftime("%Y-%m-%d")
    sql = """SELECT DISTINCT feelingNAME
            FROM feeldb.feelings f 
                JOIN feeldb.history h on f.feelingId = h.feelingId
                JOIN feeldb.users u on h.userId = u.UserId
            WHERE h.CreatedAt >= %s and h.CreatedAt < %s and u.UserId = %s
           """
    val = (from_date, to_date_plus_one, userId)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()

    list_of_feelings = [f[0] for f in myresult]
    return list_of_feelings

def find_dates_for_feeling(userId, feeling):
    mydb = make_connection.mydb_connection() 
    mycursor = mydb.cursor()
    sql = """SELECT DISTINCT DATE_FORMAT(h.CreatedAt, '%d.%m.%Y.') AS formatted_date
            FROM feeldb.feelings f 
                JOIN feeldb.history h on f.feelingId = h.feelingId
                JOIN feeldb.users u on h.userId = u.UserId
            WHERE f.feelingName = %s and u.UserId = %s 
           """
    val = (feeling, userId)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()

    list_of_dates = [d[0] for d in myresult]
    return list_of_dates

def find_dates_for_feeling_in_period(userId, dateFrom, dateTo, feeling): # want to list feeling(s) for that date
    mydb = make_connection.mydb_connection() 
    mycursor = mydb.cursor()
    from_date = datetime.strptime(dateFrom, "%d/%m/%Y").strftime("%Y-%m-%d")
    to_date_plus_one = (datetime.strptime(dateTo, "%d/%m/%Y") + timedelta(days=1)).strftime("%Y-%m-%d")
    sql = """SELECT DISTINCT DATE_FORMAT(h.CreatedAt, '%d.%m.%Y.') AS formatted_date
            FROM feeldb.feelings f 
                JOIN feeldb.history h on f.feelingId = h.feelingId
                JOIN feeldb.users u on h.userId = u.UserId
            WHERE h.CreatedAt >= %s and h.CreatedAt < %s and u.UserId = %s and f.feelingName = %s
           """
    val = (from_date, to_date_plus_one, userId, feeling)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()

    list_of_feelings = [f[0] for f in myresult]
    return list_of_feelings

