
import time
import RPi.GPIO as GPIO
import urllib.request
import json


GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.OUT)


state="off";

def loop(state):
 with urllib.request.urlopen("firebase-url.json"$
  data = json.loads(url.read().decode())
  text=(data["text"])

  if text=="light on" and state!="on":
   GPIO.output(15, GPIO.LOW);
   state="on";
  print (state)
  time.sleep(3.0)

  if text=="light off" and state !="off":
   GPIO.output(15, GPIO.HIGH);
   state="off"
  print (state)
  time.sleep(3.0)

 loop(state);

loop(state);
