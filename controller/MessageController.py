from model.MessageMethods import findMessageforFeeling

def read_message(feelingId):
    try:
        (message,color) = findMessageforFeeling(feelingId)
        return (message,color)
    except Exception as e:
        raise RuntimeError(f"Could not write message: {e}")
