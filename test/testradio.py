# Simple Raspberry PI Internet radio using four buttons
import RPi.GPIO as GPIO
import os
import atexit
from time import sleep

# Register exit routine
def finish():
    exec_command("service mpd stop")
    print("Radio stopped")

atexit.register(finish)

# Switch definitions
VOLUME_UP = 16
VOLUME_DOWN = 22
CHANNEL_UP = 12
CHANNEL_DOWN = 32

# Execute system command sub-routine
def exec_command(cmd):
     result = ""
     p = os.popen(cmd)
     for line in p.readline().split('\n'):
          result = result + line
     return result

### Main routine ###
if __name__ == "__main__":
     GPIO.setmode(GPIO.BOARD)
     GPIO.setup(VOLUME_UP,GPIO.IN)
     GPIO.setup(VOLUME_DOWN,GPIO.IN)
     GPIO.setup(CHANNEL_UP,GPIO.IN)
     GPIO.setup(CHANNEL_DOWN,GPIO.IN)
     exec_command("service mpd start")
     exec_command("mpc clear")
     exec_command("mpc load playlistradios.pls")
     exec_command("mpc play")
     exec_command("mpc volume 70")

     while True:
          newChannel = False
          if ( GPIO.input(VOLUME_UP) == False ):
               exec_command("mpc volume +4")
	       print "d"
          if ( GPIO.input(VOLUME_DOWN) == False ):
               exec_command("mpc volume -4")
	       print "c"
          if ( GPIO.input(CHANNEL_UP) == False ):
               exec_command("mpc next")
               newChannel = True
               print "b"
          if ( GPIO.input(CHANNEL_DOWN) == False ):
               exec_command("mpc prev")
               newChannel = True
	       print "a"
          if newChannel:
               current = exec_command("mpc current")
               print current
          sleep(0.2)
