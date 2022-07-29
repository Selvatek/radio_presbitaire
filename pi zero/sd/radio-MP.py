import time
import os
Magic = "http://tx.whatson.com/icecast.php?i=magic1054.mp3.m3u"
Radio1 = "http://www.listenlive.eu/bbcradio1.m3u"
current_station = Radio1
station = current_station
os.system("killall mplayer")
os.system("mplayer -playlist " + station + " &")
current_station = station
while True:
	time.sleep(10)

