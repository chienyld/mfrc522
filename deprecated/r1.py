import RPi.GPIO as GPIO
import MFRC522

MIFAREReader = MFRC522.MFRC522()  
def detect():    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
    (status,uid) = MIFAREReader.MFRC522_Anticoll()
    if status == MIFAREReader.MI_OK:
        print "Card1 Detected")
        print "Card1 read UID: %s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3])
        break