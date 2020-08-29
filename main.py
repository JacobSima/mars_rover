# Import Core or Third-party library
import os,sys

# Import Custom library
from db                              import data,manager     
from lib                             import alert                                          

# Define all paths of the programs
paths = [os.path.join(os.getcwd(),'lib'),os.path.join(os.getcwd(),'tests'),os.path.join(os.getcwd(),'db')]
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

  # Run command of series
  db_mananger.run_commands()

  # Print out the result
  db_mananger.get_rov_final()

  # Quit the program
  alert.quiting(5,True)


if __name__ == "__main__":
  main()