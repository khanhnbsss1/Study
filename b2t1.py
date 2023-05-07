import RPi.GPIO as GPIO
import time
def main():
    #define giá trị các nút bấm, dèn Led pin GPIO
    BT1 = 21
    BT2 = 26
    BT3 = 20
    BT4 = 19
    LED = 13
    GPIO.setmode(GPIO.BCM) #setup mode
    #đặt các nút bấm là input, pull_up các nút bấm
    GPIO.setup(BT1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(BT2, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(BT3, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(BT4, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    #đạt đèn led là output
    GPIO.setup(LED, GPIO.OUT)
    #đặt đènn led giấ trị HIGH
    GPIO.output(LED, GPIO.HIGH)
    ispressBT4 = False
    ispressBT3 = False
    while True:
        if GPIO.input(BT1) == GPIO.LOW: #bấm nút 1
            print("BT1 press")
            ispressBT3 = False
            GPIO.output(LED, GPIO.LOW)
            time.sleep(0.5)
        if GPIO.input(BT2) == GPIO.LOW: #bấm nút 2
            print("BT2 press")
            ispressBT3 = False
            GPIO.output(LED, GPIO.LOW)
            time.sleep(0.5)
        if GPIO.input(BT3) == GPIO.LOW: #bấm nút 3
            print("BT3 press")
            ispressBT3 = False
            GPIO.output(LED, GPIO.LOW)
            time.sleep(0.5)
        if GPIO.input(BT4) == GPIO.LOW: #bấm nút 4
            print("BT4 press")
            ispressBT3 = False
            # bấm lần 1 đèn sáng, lần 2 đèn tắt
            if ispressBT4:
                GPIO.output(LED, GPIO.HIGH)
                ispressBT4 = False
                time.sleep(0.5)
                continue
            if not ispressBT4:
                GPIO.output(LED, GPIO.LOW)
                ispressBT4 = True
                time.sleep(0.5)
                continue
            #đèn sáng nhấp nháy khi bấm bt3
            if ispressBT3:
                print("Durring Blinking")
                if GPIO.input(LED) == GPIO.LOW:
                    GPIO.output(LED, GPIO.HIGH)
                    time.sleep(1)
                if GPIO.input(LED) == GPIO.HIGH:
                    GPIO.output(LED, GPIO.LOW)
                    time.sleep(1)
try:
    main() #goi ham
except KeyboardInterrupt: #xử lí sự kiện cirl C
    GPIO.cleanup()