#!/usr/bin/env python
# -*- coding: latin-1 -*-

import RPi.GPIO as GPIO, time
import os
from RPLCD import CharLCD
GPIO.setmode(GPIO.BOARD)
from RPLCD import CharLCD

lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])
def affichage():
	GPIO.setup(Volmoins, GPIO.OUT)
	GPIO.setup(Volplus, GPIO.OUT)
	
	lcd.cursor_pos = (0, 0)
        af_test = str(test)
	lcd.write_string(af_test+"   ")
        lcd.cursor_pos = (1, 0)
        lcd.write_string("test")
        time.sleep(0.1)
        GPIO.setup(Volmoins, GPIO.IN)
	GPIO.setup(Volplus, GPIO.IN)


Volmoins = 18
Volplus = 16

GPIO.setup(Volmoins, GPIO.IN)
GPIO.setup(Volplus, GPIO.IN)
test = 0

while True:
        # Si le bouton est pressé, la broche GPIO est raccordée
        #   à la masse. Le GPIO est donc à LOW (bas).
        # Bouton pressé -> Input = LOW = False 
        if( GPIO.input( Volmoins ) == False ):
         test = test-1
	 time.sleep(0.2)
	if( GPIO.input( Volplus ) == False ):
         test = test+1
         time.sleep(0.2)
	print (test)
	affichage()
