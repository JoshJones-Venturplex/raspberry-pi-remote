import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.OUT)

try:
    while True:
        button_state = GPIO.input(23)
        if button_state == False:
            GPIO.output(17, True)
            print('Button pressed')
            time.sleep(0.2)
        else:
            GPIO.output(17, False)
except:
    GPIO.cleanup()
