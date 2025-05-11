from model.HistoryMethods import *

def handle_add_entry(feelingId, userId):
    try:
        insertIntoHistory(feelingId, userId)
    except Exception as e:
        raise RuntimeError(f"Could not write to history: {e}")
    
def formatHistory(history):
	history_formatted = []
	for (feeling, time) in history:
		history_formatted.append(time.strftime("%d.%m.%Y %H:%M:%S")+' ** '+feeling+' ** \n')
	return history_formatted
 
def read_formatted_history(userId):
    try:
        history = readHistory(userId)
        return formatHistory(history)
    except Exception as e:
        raise RuntimeError(f"Could not read from history: {e}")
    
def get_history(userId):
    return readHistory(userId)
