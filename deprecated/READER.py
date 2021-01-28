from r1 import *
from r2 import *
import signal

continue_reading = True
# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)
#import RPi.GPIO as GPIO
while continue_reading:
    detect()
    detect2()


    

