# Hey KAI!
# Voice assistant for PCs

import keyboard
import pyfiglet

class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'


def called():
  print(bcolors.BOLD+bcolors.WARNING+pyfiglet.figlet_format("KAI", font="roman"))
  input("")

if __name__ == "__main__":
  called()
  #keyboard.add_hotkey('windows+k', called)     // COMMENTED for testing purposes
  #keyboard.wait('esc')