#!/usr/bin/python

import commands as c
import pyttsx
import subprocess as sub
import time
while True:
  com='acpi -b|grep -o "[0-9]*%"'
  com1='acpi -b|grep -o "Discharging"'
  s,o=c.getstatusoutput(com)
  s1,o1=c.getstatusoutput(com1)
  o=o[:-1]
  o=int(o)
  if o1=='Discharging':
    if o<=60:
      sub.call(["notify-send","Plug the Charger.. battery "+str(o)+"%"])
      engine=pyttsx.init()
      engine.say("LowBattery")
      engine.runAndWait()
      time.sleep(5)
    else:
      sub.call(["notify-send","Battery status "+str(o)+"%"])
      time.sleep(300)  
  else:
    sub.call(["notify-send","Battery status "+str(o)+"%"])
    time.sleep(1800)
  
  
