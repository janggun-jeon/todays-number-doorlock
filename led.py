import RPi.GPIO as GPIO # 라즈베리파이의 GPIO 관련 리이브러리
import time             # 시간 관련 라이브러리

GPIO.setmode(GPIO.BCM)  # GPIO 핀들의 번호를 지정하는 규칙 설정

pin2 = 2                   # GPIO 2번핀에 대한 참조
GPIO.setup(pin2, GPIO.OUT) # 2번핀에 출력을 할 수 있도록 설정

try:                                 # 프로그램 강제종료를 인식하기 위해 try문 사용
    while True:                      # 계속 동작을 반복
        GPIO.output(pin2, GPIO.HIGH) # 2번핀의 출력을 high
        time.sleep(1)                # 1초간 상태유지
        GPIO.output(pin2, GPIO.LOW)  # 2번핀의 출력을 low
        time.sleep(1)                # 1초간 상태유지
finally:                             # 프로그램 종료할 때의 작업 실행
    GPIO.cleanup()                   # GPIO 핀들을 초기화
