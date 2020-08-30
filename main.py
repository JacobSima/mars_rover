# Import Core or Third-party library
import os,sys,time
import concurrent.futures
from subprocess import Popen, CREATE_NEW_CONSOLE

# Import Custom library
from db                              import data,manager  
  
                                         

# Define all paths of the programs
paths = [os.path.join(os.getcwd(),'lib'),os.path.join(os.getcwd(),'tests'),os.path.join(os.getcwd(),'db'),os.path.join(os.getcwd(),'img')]
for pather in paths:
  if pather not in sys.path:
    sys.path.append(pather)


# Import Custom module
from lib                                                   import msg_screen,input


def main():
  # Classes instatiate
  msg         = msg_screen.Message()
  inputText   = input.InputText()
  db_mananger = manager.Manager()

  # Display Welcoming message 
  msg.welcome()
  msg.instructions()

  # Press Enter to get started
  inputText.enter_key_pressed()

  # Display instruction for inputting the grid upper coordinates 
  msg.upper_right_msg()

  # Get user input for the upper-right coordinate
  inputText.get_upper_right_coord()

  # Display rover position and heading message
  msg.rover_msg()

  # Get rover position and heading input
  inputText.get_rover_position()

  # Display series of command instruction
  msg.command_msg()

  # Get series of user command for the rover
  inputText.get_commands()

  # Get user approval
  inputText.user_appv()

  # Use the Thread module to run both scripts
  with concurrent.futures.ThreadPoolExecutor() as executor: 
    # To continue with the script
    executor.submit(db_mananger.continue_rover_code())

    # To Run the graphic tool, pygame
    # executor.submit(Popen('cmd', creationflags=CREATE_NEW_CONSOLE))
    
    


  


if __name__ == "__main__":
  main()

  
# E.g: 5 5
# E.g: 1 2 N or 3 3 E
# E.g: LMLMLMLMM or MMRMMRMRRM