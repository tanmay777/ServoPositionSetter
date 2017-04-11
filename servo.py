import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
servoPin=11
GPIO.setup(servoPin, GPIO.OUT)
pwm=GPIO.PWM(servoPin,50)
pwm.start(7)
for i in range(0,20):
	desiredPosition=input("Where do you want the servo ?(0-180) ")
	DC=9./170.*(desiredPosition)+1
	pwm.ChangeDutyCycle(DC)	
pwm.stop()
GPIO.cleanup()

