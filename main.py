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
  TIP = '\033[38;2;190;160;95m'

kw_application = [
  "Open", "Launch", "Start", "Run", "Execute", "Boot", "Fire", "Load", "Bring up"
]

prompt = None
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
  global prompt

  print(bcolors.BOLD+bcolors.WARNING+pyfiglet.figlet_format("KAI", font="roman")+bcolors.ENDC)

  if name is None: # First meet
    print(bcolors.WARNING+"Good {morning/afternoon/evening}. This is our first time talking together. May I know your name?")
    print(bcolors.TIP+"💡 Change this later in settings")
    time.sleep(0.5)
    name = str(input(bcolors.ENDC+"You can call me: "))
    time.sleep(0.8)
    print(bcolors.WARNING+f"Hello {name}, nice to meet you. What would you like to do today?"+bcolors.ENDC)

  prompt = input("") # User sends here the intent
  actionChooser(prompt)

def actionChooser(intent):
  global kw_application

  print(f"\n{bcolors.WARNING}You wrote '{intent}'{bcolors.ENDC}")
  for p in kw_application:
    if p.lower() in intent.lower().strip():
      app = intent.replace(p, '')
      print(f"Skill {bcolors.WARNING}Application{bcolors.ENDC} has been called.")
      print(f"App: {bcolors.WARNING}{app}{bcolors.ENDC}")
      break

if __name__ == "__main__":
  keyboard.add_hotkey('windows+k', called)     # COMMENTED for testing purposes
  keyboard.add_hotkey('windows+c', bcolors_test)
  keyboard.wait('esc')