# Hey KAI!
# Voice assistant for PCs

import keyboard

def called():
  print("pressed")

if __name__ == "__main__":
  keyboard.add_hotkey('windows+k', called)
  keyboard.wait('esc')