# include libraries
import RPi.GPIO as GPIO
import time

# set gpio mode and warnings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# declare pins
trigPin = 20
echoPin = 21
redLedPin = 17
blueLedPin = 27
greenLedPin = 22

# initialize pins
GPIO.setup(trigPin,GPIO.OUT)
GPIO.setup(echoPin,GPIO.IN)
GPIO.setup(redLedPin,GPIO.OUT)
GPIO.setup(blueLedPin,GPIO.OUT)
GPIO.setup(greenLedPin,GPIO.OUT)

def get_range():
    # create a 10 microsecond pulse to trigger the ultrasonic module
    
    # set ultrasonic trigger pin to high
    GPIO.output(trigPin, True)
    # wait for 10 microsecond
    time.sleep(0.00001)
    # set ultrasonic trigger pin to low
    GPIO.output(trigPin, False)
    
    # after pulsing, we need to listen for a signal
    
    # record start time of no signal
    while GPIO.input(echoPin) == 0:
        pulse_start = time.time()
        
    # record end time of a received signal
    while GPIO.input(echoPin) == 1:
        pulse_end = time.time()
        
    # find the time difference between the signals
    pulse_duration = pulse_end - pulse_start
    
    # multiply with the speed of sound (34300 cm/s)
    # and divide by 2 to get distance, because there and back
    distance = (pulse_duration * 34300) / 2
    
    # return the calculated distance
    return distance

def show_LED(colour):
    # show only red LED
    if colour == "red":
        GPIO.output(redLedPin, True)
        GPIO.output(blueLedPin, False)
        GPIO.output(greenLedPin, False)
    # show only blue LED
    elif colour == "blue":
        GPIO.output(redLedPin, False)
        GPIO.output(blueLedPin, True)
        GPIO.output(greenLedPin, False)
    # show only green LED
    elif colour == "green":
        GPIO.output(redLedPin, False)
        GPIO.output(blueLedPin, False)
        GPIO.output(greenLedPin, True)

# main loop
while True:
    # get distance from the ultrasonic sensor
    distance = get_range()
    # print distance out and format to 2 decimal places
    print("Distance: %.2fcm" % distance)
    
    if distance < 15:
        show_LED("red")
    elif distance < 25:
        show_LED("blue")
    else:
        show_LED("green")
    
    # add some delay so the previous signal does not interfere with new signal
    time.sleep(0.1)
    
GPIO.cleanup()