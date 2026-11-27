# Hey KAI!
# Voice assistant for PCs

# IMPORTS
import keyboard
import pyfiglet
import time

# VARIABLES AND CLASSES
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

callnumber = 0
name = None

def bcolors_test():
  print(bcolors.HEADER+"HEADER")
  print(bcolors.OKBLUE + "OKBLUE")
  print(bcolors.OKCYAN + "OKCYAN")
  print(bcolors.OKGREEN + "OKGREEN")
  print(bcolors.WARNING + "WARNING")
  print(bcolors.FAIL + "FAIL")
  print(bcolors.ENDC)
  print(bcolors.BOLD + "BOLD")
  print(bcolors.UNDERLINE + "UNDERLINE")

def called():
  global name
  print(bcolors.BOLD+bcolors.WARNING+pyfiglet.figlet_format("KAI", font="roman")+bcolors.ENDC)
  if name is None:
    print(bcolors.WARNING+"Good {morning/afternoon/evening}. This is our first time talking together. May I know your name?")
    time.sleep(0.5)
    name = str(input(bcolors.ENDC+"You can call me: "))
    time.sleep(0.8)
    print(bcolors.WARNING+f"Hello {name}, nice to meet you. What would you like to do today?")

if __name__ == "__main__":
  called()
  bcolors_test()
  #keyboard.add_hotkey('windows+k', called)     // COMMENTED for testing purposes
  #keyboard.wait('esc')