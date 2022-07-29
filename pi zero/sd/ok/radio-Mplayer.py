# Simple Raspberry PI Internet radio using four buttons
import alsaaudio
import RPi.GPIO as GPIO
import os
import time
import atexit
from time import sleep
from RPLCD import CharLCD
lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])

# Switch definitions
SHUTDOWN = 7
VOLUME_UP = 16
VOLUME_DOWN = 22
CHANNEL_UP = 12
CHANNEL_DOWN = 32
sta = 1
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
station10 = "http://185.52.127.173/fr/30001/mp3_128.mp3?origine=fluxradios"
title10 = "NRJ"
play_station = station1
title = title1
#routine
GPIO.setmode(GPIO.BOARD)
GPIO.setup(VOLUME_UP,GPIO.IN)
GPIO.setup(VOLUME_DOWN,GPIO.IN)
GPIO.setup(CHANNEL_UP,GPIO.IN)
GPIO.setup(CHANNEL_DOWN,GPIO.IN)
GPIO.setup(SHUTDOWN,GPIO.IN)
os.system("killall mplayer")
os.system("mplayer"+" "+play_station+" &")
m = alsaaudio.Mixer('MPC')
vol = m.getvolume()
vol = 24
m.setvolume(vol)
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
	global vol
	global title
	lcd.cursor_pos = (0, 0)
        lcd.write_string("                ")
	lcd.cursor_pos = (0, 0)
	lcd.write_string(title)
        lcd.cursor_pos = (1, 0)
        lcd.write_string("volume"+": "+str(vol)+"%"+"     ")
affichage()
while True:
         # newChannel = False
          if ( GPIO.input(VOLUME_UP) == False ):
		if vol < 100:
			vol = vol + 2
			m.setvolume(vol)
			affichage()
          if ( GPIO.input(VOLUME_DOWN) == False ):
		if vol > 0:
			vol = vol - 2
                	m.setvolume(vol)
			affichage()
          if ( GPIO.input(CHANNEL_UP) == False ):
		if sta < 10:
			sta = sta + 1
			print sta
			station()
			affichage()
          if ( GPIO.input(CHANNEL_DOWN) == False ):
		if sta > 1:
			sta = sta - 1
			print sta
			station()
			affichage()
          if ( GPIO.input(SHUTDOWN) == False ):
               test = m.getenum()
	       print test
	  time.sleep(0.1)
