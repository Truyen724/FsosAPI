try:
    import RPi.GPIO as GPIO#
    import time

    PORT_GPIO = 21
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PORT_GPIO, GPIO.OUT)


    def den_on(PORT_GPIO):
        GPIO.output(PORT_GPIO,GPIO.HIGH)
        
    def den_off(PORT_GPIO):
        GPIO.output(PORT_GPIO,GPIO.LOW)
except:
    pass    
# if(__name__ == "__main__"):
#     try:
#         den_on(PORT_GPIO)
#         time.sleep(1)
#         den_off(PORT_GPIO)
#         time.sleep(1)
#         GPIO.cleanup()
#     except KeyboardInterrupt:
#         GPIO.cleanup()
#         pass
