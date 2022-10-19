import RPi.GPIO as GPIO
from time import sleep

servopin = 32
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servopin, GPIO.OUT)

pi_pwm = GPIO.PWM(servopin, 333)
pi_pwm.start(0)

while True:
	pi_pwm.ChangeDutyCycle(5)
	sleep(5)
	pi_pwm.ChangeDutyCycle(50)
	sleep(5)
	pi_pwm.ChangeDutyCycle(75)
	sleep(5)
	pi_pwm.ChangeDutyCycle(100)
	sleep(5)
