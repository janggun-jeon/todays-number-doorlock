import random
import keypad as kp

symbols = "0123456789*#"

def todayNumber():
    data = ""
    for itr in range(kp.passwdLength):
        idx = random.randrange(len(symbols))
        data = data + symbols[idx]
    return data
    