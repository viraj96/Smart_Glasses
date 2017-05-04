def reading(sensor):
    import time
    import RPi.GPIO as GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    if sensor == 0:
        GPIO.setup(17,GPIO.OUT)
        GPIO.setup(27,GPIO.IN)
        GPIO.output(17, GPIO.LOW)
        time.sleep(0.3)
        GPIO.output(17, True)
        time.sleep(0.00001)
        GPIO.output(17, False)
        while GPIO.input(27) == 0:
          signaloff = time.time()
        while GPIO.input(27) == 1:
          signalon = time.time()
        timepassed = signalon - signaloff
        distance = timepassed * 17000
        return distance
        GPIO.cleanup()
    else:
        print "Incorrect usonic() function varible."
print reading(0)