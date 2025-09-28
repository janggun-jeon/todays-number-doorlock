import RPi.GPIO as GPIO
import time
import signal
import datetime
from  exception import TimeOutException
import moter as mt
import keypad as kp
import number_of_main as nm
import number_of_today as nt
import warnings

warnings.filterwarnings('ignore')

day = 24 * 60 * 60 # 시 * 분 * 초
reset_cnt=0
target_date=datetime.datetime(2023,1,1,23,59,0)

passwd = ["", ""]
passwd[0] = nm.mainNumber()
passwd[1] = nt.todayNumber()
print('오늘의 번호 갱신!\n', passwd, '\n')

def check_date():
    global target_date
    current_date=datetime.datetime.now()
    
    if current_date >= target_date:
        while current_date >= target_date:
            target_date=target_date+datetime.timedelta(seconds=day)
        
        return (target_date-current_date).total_seconds()
    else:
        return (target_date - current_date).total_seconds()
        

def alarm_handler(signum, frame):
    passwd[1] = nt.todayNumber()
    print('오늘의 번호 갱신!\n', passwd)
    raise KeyboardInterrupt()

def doorlock():
    global reset_cnt
    while True:
        try:    
            flag = int(check_date()) + 1
            signal.signal(signal.SIGALRM, alarm_handler)
            signal.alarm(flag)
            key = kp.keypad()
            print("key는 ", key, '\n')
            if key in passwd:
                time.sleep(2)
                mt.unlock()
                time.sleep(7)
                mt.lock()
                print("Open")
                
            elif key == None:    
                continue
            elif key == "TimeOutException":
                raise TimeOutException()
            elif key == "closeDoor":
                mt.lock()
                print("Close")          
        except TimeOutException as e:

            continue
        except KeyboardInterrupt:

            continue

doorlock()
