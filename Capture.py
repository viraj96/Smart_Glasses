import RPi.GPIO as GPIO
import picamera
import time

GPIO.setwarnings(False)

#Access Button
GPIO.setmode(GPIO.BCM)
buttonPin = 17
GPIO.setup(buttonPin, GPIO.IN, GPIO.PUD_DOWN)

#Access Red LED
LED = 4
GPIO.setup(LED, GPIO.OUT)

#Intializing Pi Camera
camera = picamera.PiCamera()

print("Press button to take picture, CTRL+C to exit")

while True:
        if GPIO.input(buttonPin): #Button Pressed 
               print("Button pressed...Picture Taken")

               #Light Red
               GPIO.output(LED, True)
               time.sleep(1)
               GPIO.output(LED, False)

               #Take picture
               camera.capture('/home/pi/Desktop/Scanner/image.jpg')
               camera.close()