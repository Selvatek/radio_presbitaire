# Simple Raspberry PI utilisant deux potentiometres

import alsaaudio
import RPi.GPIO as GPIO
import os
import time
import atexit
from time import sleep
from RPLCD import CharLCD
lcd = CharLCD(cols=16, rows=2, pin_rs=26, pin_e=19, pins_data=[13, 6, 5, 21], numbering_mode=GPIO.BCM)
from gpiozero import MCP3008
import time

#Definitions des variables
pot = MCP3008(0)
pot2 = MCP3008(1)
count = 0
potradio = round(pot.value, 2)
oldpotradio = 0
oldradio = 0
radio = 0
vol = 0
oldvol = 0

# Numero des pins
VOLUME_UP = 23
VOLUME_DOWN = 25
CHANNEL_UP = 18
CHANNEL_DOWN = 12
sta = 1

#Les differentes stations radios
station0 = "http://streaming.radio.rtl.fr/rtl-1-48-192"
title0 = "RTL"
station1 = "http://chai5she.cdn.dvmr.fr/franceinter-midfi.mp3"
title1 = "France Inter"
station2 = "http://185.52.127.160/fr/30401/mp3_128.mp3?origine=fluxradios"
title2 = "Rire et Chanson"
station3 = "http://chai5she.cdn.dvmr.fr/franceinfo-midfi.mp3"
title3 = "France Info"
station4 = "http://chai5she.cdn.dvmr.fr/franceculture-midfi.mp3"
title4 = "France Culture"
station5 = "http://chai5she.cdn.dvmr.fr/francemusique-midfi.mp3"
title5 = "France Musique"
station6 = "http://chai5she.cdn.dvmr.fr/fip-midfi.mp3"
title6 = "Fip"
station7 = "http://novazz.ice.infomaniak.ch/novazz-128.mp3"
title7 = "Nova"
station8 = "http://chai5she.cdn.dvmr.fr/mouv-midfi.mp3"
title8 = "Mouv"
station9 = "http://185.52.127.163/fr/30601/mp3_128.mp3?origine=fluxradios"
title9 = "Nostalgie"
station10 = "http://radiomeuh.ice.infomaniak.ch/radiomeuh-64.aac.m3u"
title10 = "Meuh"
play_station = station1
title = title1

#Lancement de la radio
GPIO.setmode(GPIO.BCM)
GPIO.setup(VOLUME_UP,GPIO.IN)
GPIO.setup(VOLUME_DOWN,GPIO.IN)
GPIO.setup(CHANNEL_UP,GPIO.IN)
GPIO.setup(CHANNEL_DOWN,GPIO.IN)
GPIO.setup(SHUTDOWN,GPIO.IN)

os.system("killall mplayer")
os.system("mplayer"+" "+play_station+" &")
m = alsaaudio.Mixer('PCM')


def station():
 	global sta
	global play_station
	global station1
	global station2
	global station3
	global station4
	global station5
	global station6
	global station7
	global station8
	global station9
	global station10
	global title
	global title1
	global title2
	global title3
        global title4
        global title5
	global title6
        global title7
        global title8
	global title9
        global title10
	if sta == 0:
		play_station = station0
		title = title0
	if sta == 1:
		play_station = station1
		title = title1
	if sta == 2:
        	play_station = station2
		title = title2
	if sta == 3:
        	play_station = station3
		title = title3
	if sta == 4:
                play_station = station4
		title = title4	
	if sta == 5:
                play_station = station5
		title = title5
	if sta == 6:
                play_station = station6
		title = title6
	if sta == 7:
                play_station = station7
		title = title7
	if sta == 8:
                play_station = station8
		title = title8
	if sta == 9:
                play_station = station9
		title = title9
	if sta == 10:
                play_station = station10
		title = title10
	os.system("killall mplayer")
	os.system("mplayer"+" "+play_station+" &")


def affichage():

	#Gpio en output suite a un bug en BCm	
	GPIO.setup(VOLUME_UP,GPIO.OUT)
	GPIO.setup(VOLUME_DOWN,GPIO.OUT)
	GPIO.setup(CHANNEL_UP,GPIO.OUT)
	GPIO.setup(CHANNEL_DOWN,GPIO.OUT)
	GPIO.setup(SHUTDOWN,GPIO.OUT)

	#import des variables utilisees dans affichage
	global vol
	global title
	lcd.cursor_pos = (0, 0)
        lcd.write_string("                ")
	lcd.cursor_pos = (0, 0)
	lcd.write_string(title)
        lcd.cursor_pos = (1, 0)
        lcd.write_string("volume"+": "+str(vol)+"%"+"    ")

	#Remettre les gpio en input avant de sortir d affichage
	GPIO.setup(VOLUME_UP,GPIO.IN)
	GPIO.setup(VOLUME_DOWN,GPIO.IN)
	GPIO.setup(CHANNEL_UP,GPIO.IN)
	GPIO.setup(CHANNEL_DOWN,GPIO.IN)
	GPIO.setup(SHUTDOWN,GPIO.IN)

# lancement du premier affichage
affichage()
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
     
        #changement de station radio
	if count == 3 and radio != oldradio:
                print "changement"
		sta = radio
                station()
                affichage()
		oldradio = radio
	
	#
        oldpotradio = potradio
	#releve du potentiometre volume
	vol = int(round(pot2.value *100))
	oldvol = int(oldvol)
	if vol != oldvol:	
		m.setvolume(vol)
                affichage()
		oldvol = vol
        time.sleep(0.1)
