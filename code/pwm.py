import RPi.GPIO as GPIO # 라즈베리파이의 GPIO 관련 리이브러리
import time             # 시간 관련 라이브러리

GPIO.setmode(GPIO.BCM)  # GPIO 핀들의 번호를 지정하는 규칙 설정

pin2 = 2                   # GPIO 2번핀에 대한 참조
GPIO.setup(pin2, GPIO.OUT) # 2번핀에 출력을 할 수 있도록 설정
pwm = GPIO.PWM(pin2, 1000) # 2번핀에 1000hz의 pwm 출력을 하는 stred 설정 및 참조 반환
pwm.start(0)

try:                             # 프로그램 강제종료를 인식하기 위해 try문 사용
    while True:                  # 계속 동작을 반복
        pwm.ChangeDutyCycle(0)   # pwm 출력의 듀티사이클을 0%로 (출력 0)
        time.sleep(1)            # 1초간 상태유지
        pwm.ChangeDutyCycle(10)  # pwm 출력의 듀티사이클을 10%로
        time.sleep(1)            # 1초간 상태유지
        pwm.ChangeDutyCycle(20)  # pwm 출력의 듀티사이클을 20%로
        time.sleep(1)            # 1초간 상태유지
        pwm.ChangeDutyCycle(30)  # pwm 출력의 듀티사이클을 30%로
        time.sleep(1)            # 1초간 상태유지
        pwm.ChangeDutyCycle(40)  # pwm 출력의 듀티사이클을 40%로
        time.sleep(1)            # 1초간 상태유지
        pwm.ChangeDutyCycle(50)  # pwm 출력의 듀티사이클을 50%로
        time.sleep(1)            # 1초간 상태유지
        pwm.ChangeDutyCycle(60)  # pwm 출력의 듀티사이클을 60%로
        time.sleep(1)            # 1초간 상태유지
        pwm.ChangeDutyCycle(70)  # pwm 출력의 듀티사이클을 70%로
        time.sleep(1)            # 1초간 상태유지
        pwm.ChangeDutyCycle(80)  # pwm 출력의 듀티사이클을 80%로
        time.sleep(1)            # 1초간 상태유지
        pwm.ChangeDutyCycle(90)  # pwm 출력의 듀티사이클을 90%로
        time.sleep(1)            # 1초간 상태유지
        pwm.ChangeDutyCycle(100) # pwm 출력의 듀티사이클을 1000%로 (출력 1)
        time.sleep(1)            # 1초간 상태유지
finally:                         # 프로그램 종료할 때의 작업 실행
    GPIO.cleanup()               # GPIO 핀들을 초기화