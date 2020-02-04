import sys
import os
from playsound import playsound


sounds = []
directory = "farts"
for filename in os.listdir(directory):
  if filename.endswith(".mp3"):
    sounds.append (os.path.join(directory, filename))

for i in sys.argv[1]:
  print (i)
  playsound(sounds[ord(i) % len (sounds)])
