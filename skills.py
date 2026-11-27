from main import bcolors
import subprocess

# Skills keywords
kw_application = [
  "Open", "Launch", "Start", "Run", "Execute", "Boot", "Fire", "Load", "Bring up"
]

# ACTION CHOOSER - SKILL ROUTER
def actionChooser(intent):
  global kw_application

  print(f"\n{bcolors.WARNING}You wrote '{intent}'{bcolors.ENDC}")
  for p in kw_application:
    if p.lower() in intent.lower().strip():
      app = intent.replace(p.lower(), '').strip()
      print(f"Skill {bcolors.WARNING}Application{bcolors.ENDC} has been called.")
      print(f"App: {bcolors.WARNING}{app}{bcolors.ENDC}")
      openApplication(app)
      break

# SKILLS Behaviors
def openApplication(app):
  try:
    subprocess.Popen([app])
    print(f"{bcolors.TIP}{app} opened.{bcolors.ENDC}")
  except FileNotFoundError:
    print(f"{bcolors.WARNING}App not found.{bcolors.ENDC}")