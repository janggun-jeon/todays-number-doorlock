import RPi.GPIO as GPIO # 라즈베리파이의 GPIO 관련 리이브러리
import time             # 시간 관련 라이브러리
import warnings

warnings.filterwarnings('ignore')

#### 모터 설정 ####

# 모터 번호(추가 가능)
CH = 0

# 모터 PWM 주파수
freq = 50

# 모터 동작 종류
STOP     = 0
FORWARD  = 1
BACKWORD = 2

# 모터 dutyCycle
min_duty = 1
max_duty = 80


#### GPIO pin 설정 ####

# 모터 PWM enable 핀
Enable_pin = 26  #37 pin

# 모터 동작 제어 핀
forward_pin = 19  #37 pin
backward_pin = 13  #35 pin


#### 사용자 정의 함수들 ####

# 회전각 만큼의 dutyCycle 정도를 계산
def degreeProcessing(degree):
    # 최대 회전각 90도, 최소 회전각 0도
    if degree > 90:
        degree = 180
    elif degree < 0:
        degree = 0
    
    return min_duty + (degree * (max_duty - min_duty) / 180.0)
    

# 모터 제어 함수
def setMotorControl(pwm, forward_pin, backward_pin, degree, action):
    #모터 회전 제어
    duty = degreeProcessing(degree)
    pwm.ChangeDutyCycle(duty)  
    
    # 정방향 회전
    if action == FORWARD:
        GPIO.output(forward_pin, GPIO.HIGH)
        GPIO.output(backward_pin, GPIO.LOW)
        
    # 역방향 회전
    elif action == BACKWORD:
        GPIO.output(forward_pin, GPIO.LOW)
        GPIO.output(backward_pin, GPIO.HIGH)
        
    # 회전을 멈춤
    elif action == STOP:
        GPIO.output(forward_pin, GPIO.LOW)
        GPIO.output(backward_pin, GPIO.LOW)

        
# 모터 제어 설정 함수
def setMotor(ch, degree, action):
    # 모터 번호에 따라 적절한 핀들을 선택해서 제어함수 호출
    if ch == CH:
        setMotorControl(pwm, forward_pin, backward_pin, degree, action)
  
# 핀 설정 초기화
def setPinConfig(EN, INA, INB):        
    GPIO.setup(EN, GPIO.OUT)
    GPIO.setup(INA, GPIO.OUT)
    GPIO.setup(INB, GPIO.OUT)
    
    pwm = GPIO.PWM(EN, freq)    
    pwm.start(0) 
    
    return pwm

def lock():
    setMotor(CH, 90, FORWARD)
    time.sleep(0.3)
    setMotor(CH, 90, STOP)
    time.sleep(1.5)
    
def unlock():
    # 역방향으로 90도 회전 후 잠깐 대기
    setMotor(CH, 90, BACKWORD)
    time.sleep(3)
    setMotor(CH, 90, STOP)
    time.sleep(1.5)



#### 프로그램 실행 ####

# GPIO 핀들의 번호를 지정하는 모드 설정
GPIO.setmode(GPIO.BCM)

#모터와 핀 바인딩 후, 모터 PWM enable 스레드(thread)의 참조를 반환
pwm = setPinConfig(Enable_pin, forward_pin, backward_pin)



if __name__ == "__main__":
    #제어 시작

    # 정방향으로 90도 회전 후 잠깐 대기
    setMotor(CH, 90, FORWARD)
    time.sleep(0.3)
    setMotor(CH, 90, STOP)
    time.sleep(1.5)

    # 역방향으로 90도 회전 후 잠깐 대기
    setMotor(CH, 90, BACKWORD)
    time.sleep(3)
    setMotor(CH, 90, STOP)
    time.sleep(1.5)

    # 정방향으로 90도 회전 후 잠깐 대기
    setMotor(CH, 90, FORWARD)
    time.sleep(0.3)
    setMotor(CH, 90, STOP)
    time.sleep(1.5)

    # 역방향으로 90도 회전 후 잠깐 대기
    setMotor(CH, 90, BACKWORD)
    time.sleep(3)
    setMotor(CH, 90, STOP)
    time.sleep(1.5)

    # 정방향으로 90도 회전 후 잠깐 대기
    setMotor(CH, 90, FORWARD)
    time.sleep(0.3)
    setMotor(CH, 90, STOP)
    time.sleep(1.5)

    # 역방향으로 90도 회전 후 잠깐 대기
    setMotor(CH, 90, BACKWORD)
    time.sleep(3)
    setMotor(CH, 90, STOP)
    time.sleep(1.5)

    # 정방향으로 90도 회전 후 잠깐 대기
    setMotor(CH, 90, FORWARD)
    time.sleep(0.3)
    setMotor(CH, 90, STOP)
    time.sleep(1.5)

    # 역방향으로 90도 회전 후 잠깐 대기
    setMotor(CH, 90, BACKWORD)
    time.sleep(3)
    setMotor(CH, 90, STOP)
    time.sleep(1.5)

    # 종료
    GPIO.cleanup()

    print("성공적으로 프로그램이 수행됨")

