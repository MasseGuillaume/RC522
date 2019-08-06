#!/usr/bin/env python
import time

# time.sleep(1)
print("hello2")



import RPi.GPIO as GPIO
from mfrc522loco import SimpleMFRC522

GPIO.setwarnings(False)


print("reader")
reader = SimpleMFRC522()
print("after reader")

try:
  while True:
    print("reading")
    id, text = reader.read()
    print('id: ' + str(id))
    print('text: ' + text)
    time.sleep(1)
# except:
#   print('yo')

finally:
  print('cleanup')
  GPIO.cleanup()
