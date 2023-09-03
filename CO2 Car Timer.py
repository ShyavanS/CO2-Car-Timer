import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def timer():
    start = True
    left = True
    right = True
    while start == True or left == True or right == True:
        if GPIO.input(23) == 0 and start == True:
            starttime = (time.time())
            print("Timer has started")
            start = False
        if GPIO.input(21) == 0 and left == True:
            racetime1 = (time.time())
            difftime1 = racetime1 - starttime
            print("Car A:", "Time -", difftime1, "sec.",
                  "Speed -", 15.5 / difftime1 * 3.6, "km/h")
            left = False
        if GPIO.input(16) == 0 and right == True:
            racetime2 = (time.time())
            difftime2 = racetime2 - starttime
            print("Car B:", "Time -", difftime2, "sec.",
                  "Speed -", 15.5 / difftime2 * 3.6, "km/h")
            right = False
    query = input("Restart timer? <y/n> ")
    if query == "Y" or "y":
        timer()
    elif query == "N" or "n":
        GPIO.cleanup()
        exit()


timer()
