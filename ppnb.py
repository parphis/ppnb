import os
import menu

# Main Program
if __name__ == "__main__":
  clear = lambda: os.system('cls')
  clear()
  print (">>>Hello<<<")
  print ("***")
  # Launch main menu
  menu.main_menu()