import RPi.GPIO as GPIO
import MFRC52202
#import signal
MIFAREReader2 = MFRC52202.MFRC52202() 
def detect2():     
    (status2,TagType2) = MIFAREReader2.MFRC522_Request(MIFAREReader2.PICC_REQIDL)
    (status2,uid2) = MIFAREReader2.MFRC522_Anticoll()
    if status2 == MIFAREReader2.MI_OK:
        print "Card2 Detected")
        print "Card2 read UID: %s,%s,%s,%s" % (uid2[0], uid2[1], uid2[2], uid2[3])
        break