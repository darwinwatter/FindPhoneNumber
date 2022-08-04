def checkNumberRus(text):
    if len(text) != 15:
       return False
    if text[0] != '7':
        return False
    if text[1] != '(':
        return False
    for i in range(2,5):
        if not text[i].isdecimal():
            return False
    if text[5] != ')':
        return False
    for i in range(6,9):
        if not text[i].isdecimal():
            return False
    if text[9] != '-':
        return False
    for i in range(10,12):
        if not text[i].isdecimal():
            return False
    if text[12] != '-':
        return False
    for i in range(13,15):
        if not text[i].isdecimal():
            return False
    return True

def checkNumberBy(text):
    if len(text) != 16:
       return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '(':
        return False
    for i in range(4,6):
        if not text[i].isdecimal():
            return False
    if text[6] != ')':
        return False
    for i in range(7,10):
        if not text[i].isdecimal():
            return False
    if text[10] != '-':
        return False
    for i in range(11,13):
        if not text[i].isdecimal():
            return False
    if text[13] != '-':
        return False
    for i in range(14,16):
        if not text[i].isdecimal():
            return False
    return True