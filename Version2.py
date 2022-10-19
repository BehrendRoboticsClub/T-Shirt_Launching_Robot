import board
import neopixel
import time
pixels = neopixel.NeoPixel(board.D18, 30)

pixels[0] = (0,0,0)
time.sleep(1)

count = 0
while (count < 10):
	pixels[0] = (255,0,0)
	time.sleep(.1)
	pixels[0] = (0,0,0)
	pixels[1] = (255,255,0)
	time.sleep(.1)
	pixels[1] = (0,0,0)
	pixels[2] = (0,0,255)
	time.sleep(.1)
	pixels[2] = (0,0,0)
	pixels[3] = (0,255,0)
	time.sleep(.1)
	pixels[3] = (0,0,0)
	pixels[4] = (125, 200, 50)
	time.sleep(.1)
	pixels[4] = (0, 0, 0)
	pixels[5] = (0,255,0)
	time.sleep(.1)
	pixels[5] = (0,0,0)
	count = count + 1
