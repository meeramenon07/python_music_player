from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False
  while True:
    stop_playback = int(input("Press 2 anytime to stop playback and go back to the Menu : "))
    if stop_playback == 2:
      source.paused = True
      return
      
      
    else:
      continue
while True:
  os.system("clear")
  print("My POD Music Player")
  time.sleep(1)
  print("Press 1 to play")
  time.sleep(1)
  print("press anything else to see the menu again!")
  userInput = int(input())
  if userInput == 1:
    print("playing some tunes.")
    play()
  elif UserInput == 2:
    exit()
  else:
    continue
  
