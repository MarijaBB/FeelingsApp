from model.SearchMethods import *

def read_search_results(userId, feelingName, from_date, to_date):
    return find_entries(userId, feelingName, from_date, to_date)