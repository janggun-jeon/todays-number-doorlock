
import RPi.GPIO as GPIO
import time
import signal
from  exception import TimeOutException
import warnings

warnings.filterwarnings('ignore')


R1 = 7
R2 = 8
R3 = 25
R4 = 24

C1 = 23
C2 = 18
C3 = 15
C4 = 14

L = [5, 12, 16, 20, 21]

passwd = []
passwdLength = 4
passwdCount = 1
timeout = 20
# Initialize the GPIO pins

#GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(R1, GPIO.OUT)
GPIO.setup(R2, GPIO.OUT)
GPIO.setup(R3, GPIO.OUT)
GPIO.setup(R4, GPIO.OUT)

GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(L[0], GPIO.OUT)
GPIO.setup(L[1], GPIO.OUT)
GPIO.setup(L[2], GPIO.OUT)
GPIO.setup(L[3], GPIO.OUT)
GPIO.setup(L[4], GPIO.OUT)

def readLine(line, characters, count):
    global passwd
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(C1) == 1):
        print(characters[0], '\n')
        passwd.append(characters[0])
        GPIO.output(L[count], GPIO.HIGH)
        count = count + 1
    if(GPIO.input(C2) == 1):
        print(characters[1], '\n')
        passwd.append(characters[1])
        GPIO.output(L[count], GPIO.HIGH)
        count = count + 1
    if(GPIO.input(C3) == 1):
        print(characters[2], '\n')
        passwd.append(characters[2])
        GPIO.output(L[count], GPIO.HIGH)
        count = count + 1
    if(GPIO.input(C4) == 1):
        print(characters[3], '\n')
        passwd.append(characters[3])
        GPIO.output(L[count], GPIO.HIGH)
        count = count + 1
    GPIO.output(line, GPIO.LOW)
    return count


def open_button():
    GPIO.output(R1, GPIO.HIGH)
    if(GPIO.input(C4) == 1):
        GPIO.output(L[0], GPIO.HIGH)
        GPIO.output(R1, GPIO.LOW)
        return True
    GPIO.output(R1, GPIO.LOW)
    return False

def close_button():
    GPIO.output(R2, GPIO.HIGH)
    if(GPIO.input(C4) == 1):
        GPIO.output(L, GPIO.HIGH)
        GPIO.output(R2, GPIO.LOW)
        return True
    GPIO.output(R2, GPIO.LOW)
    return False

def alarm_handler(signum, frame):
    print("\nTime Out!")
    raise TimeOutException()

def keypad(count=passwdCount):
    global passwd
    try:
        while True:
    
            if open_button():
                print('입장 버튼 누름')
                time.sleep(0.25)
                signal.signal(signal.SIGALRM, alarm_handler)
                signal.alarm(timeout)
                while count <= passwdLength:
                    count = readLine(R1, ["1","2","3","A"], count)
                    count = readLine(R2, ["4","5","6","B"], count)
                    count = readLine(R3, ["7","8","9","C"], count)
                    count = readLine(R4, ["*","0","#","D"], count)
                    time.sleep(0.25)
                GPIO.output(L, GPIO.LOW)
                key = ''.join(s for s in passwd)
                passwd = []
                signal.alarm(0)
                return key
            elif close_button():
                print('퇴장 버튼 누름')
                GPIO.output(L, GPIO.LOW)
                time.sleep(0.25)
                key = "closeDoor"
                return key
    except KeyboardInterrupt:
        GPIO.output(L, GPIO.LOW)
        passwd = []
        print("System Interrupt!")  
        return "TimeOutException"
    except TimeOutException as e: 
        GPIO.output(L, GPIO.LOW)
        passwd = []
        return None

if __name__ == "__main__":       
    key = keypad()  
    if key == None: 
        print('None')
