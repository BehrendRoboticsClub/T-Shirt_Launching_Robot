import RPi.GPIO as GPIO
from time import sleep

servopin = 32
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servopin, GPIO.OUT)

pi_pwm = GPIO.PWM(servopin, 333)		#assigns pin to new pwm instance with frequency of 333 Hz
pi_pwm.start(0)					#starts pwm at duty cycle 0%

while True:
	pi_pwm.ChangeDutyCycle(5)		#changes duty cycle to inputed value (0-100%), this sets duty cycle to 5%
	sleep(5)				#delay for 5 seconds
	pi_pwm.ChangeDutyCycle(50)
	sleep(5)
	pi_pwm.ChangeDutyCycle(75)
	sleep(5)
	pi_pwm.ChangeDutyCycle(100)
	sleep(5)
