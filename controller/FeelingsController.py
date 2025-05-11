from model.FeelingsMethods import *

def read_feeling_name(feelingId):
    try:
        return getFeelingName(feelingId)
    except Exception as e:
        raise RuntimeError(f'Can\'t get feeling name: {e}')

def get_image(feelingId):
    try:
        return getImage(feelingId)
    except Exception as e:
            raise RuntimeError(f'Can\'t get feeling name: {e}')