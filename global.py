def _init():
    global FilePath
    FilePath = {}

def setValue(key,value):
    FilePath[key] = value

def getValue(key):
    try:
        return FilePath
    except KeyError:
        return None
