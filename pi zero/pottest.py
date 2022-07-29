from gpiozero import MCP3008
import time
pot = MCP3008(0)
pot2 = MCP3008(1)
print pot.value
count = 0
oldpotradio = 0
oldradio = 0
radio = 0
while True:
	potradio= round(pot.value, 2)
	if oldpotradio != potradio:
		if  potradio == 1.0:
			radio = 10
		elif potradio == 0.99:
			radio = 9
		elif potradio == 0.97:
			radio = 8
		elif potradio == 0.95:
			radio = 7
		elif potradio == 0.9:
			radio = 6
		elif potradio == 0.81:
			radio = 5 
		elif potradio == 0.73:
			radio = 4
		elif potradio == 0.57:
			radio = 3
		elif potradio == 0.58:
			radio = 3
		elif potradio == 0.32:
			radio = 2
		elif potradio == 0.33:
			radio = 2
		elif potradio == 0.07:
			radio = 1
		elif potradio == 0.08:
			radio = 1
		elif potradio == 0.0:
			radio = 0
	if potradio == oldpotradio:
		count = count+1
	if potradio != oldpotradio:
		count = 0
	if count == 3 and radio != oldradio:
		print "changement ----------------------------------"
		oldradio = radio
	print radio
	print potradio
	oldpotradio = potradio
	time.sleep(0.1)

