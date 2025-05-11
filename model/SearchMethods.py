from model import make_connection
from datetime import datetime, timedelta

def find_entries(userId, feeling=None, from_date=None, to_date=None):
    mydb = make_connection.mydb_connection() 
    cursor = mydb.cursor()
    
    query = """SELECT DISTINCT DATE_FORMAT(h.CreatedAt, '%d.%m.%Y.') AS formatted_date, feelingNAME
                FROM feeldb.feelings f 
                JOIN feeldb.history h on f.feelingId = h.feelingId
                JOIN feeldb.users u on h.userId = u.UserId
                WHERE u.userid = %s"""
    params = [userId]
    
    if feeling:
        query += " AND feelingName = %s"
        params.append(feeling)
    if from_date and to_date:
        from_date = datetime.strptime(from_date, "%d/%m/%Y").strftime("%Y-%m-%d")
        to_date = (datetime.strptime(to_date, "%d/%m/%Y") + timedelta(days=1)).strftime("%Y-%m-%d")
        query +=" AND h.CreatedAt >= %s and h.CreatedAt < %s"
        params.extend([from_date, to_date])

    cursor.execute(query, tuple(params))
    rows = cursor.fetchall()
    cursor.close()

    # Decide what to return based on input
    results = []
    for date, logged_feeling in rows:
        if feeling and from_date and to_date:
            results.append(str(date))  # matching feeling in range → return date
        elif feeling:
            results.append(str(date))  # feeling only → return date
        elif from_date and to_date:
            results.append(f"{date} - {logged_feeling}")  # range only → return both

    return results