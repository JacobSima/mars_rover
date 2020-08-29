# Import Core or Third-party library
import socket,getpass,datetime,os


# printed Message to be displayed on the screen
class Message():


  def __init__(self):
    pass


  # Mars Main Introduction and Welcome Message
  def welcome(self):
    
    # Get machine current logged user
    username  = getpass.getuser()

    # Get Current time
    dt_now    = datetime.datetime.now()

    # Define current time for greeting
    msg       = ''
    space     = ''
    morning   = (1,2,3,4,5,6,7,8,9,10,11)
    Afternoon = (12,13,14,15,16,17)
    evening   = (18,19,20)
    night     = (21,22,23,24)
    
    # Logic of the greeting statement
    if dt_now.hour in morning:
      msg   = 'Good Monring'
      space = '  '
    elif dt_now.hour in Afternoon:
      msg   = 'Good Afternoon'
    elif dt_now.hour in night:
      msg   = 'Good Night'
      space = '    '
    elif dt_now.hour in evening:
      msg   = 'Good Evening'
      space = '  '


    # Clean the screen, just like typing clear on CMD
    os.system('clear')

    # Printing 
    print('****************** MARS ROVER PROGRAM  ********************')
    print('***                                                     ***')
    print(f'***  {msg} {username}, Welcome to the MARS ROVER    {space}***')
    print('***                                                     ***')
    print('*'*59)
  
  
  # Define program instruction
  def instructions(self):
    print('\n')
    print('********************************** INSTRUCTIONS *******************************************')
    print('* Mars program requires the User to corretly follow the below instruction                 *')
    print('*                                                                                         *')
    print('*        Step 1 => Enter the UPPER-RIGHT Coordinate of the GRID                           *')
    print('*                  The BOTTOM-LEFT coordinate of the grid is (0,0)                        *')
    print('*     NB : Grid can have ONE or SEVERAL Rovers                                            *')
    print('*        Step 2 => Enter the rover position and heading                                   *')
    print('*        Step 3 => Enter series of instructions telling the rover how to explore the grid *')
    print('*                                                                                         *')
    print('* You can orderly repeat step 2 and 3 several times as the grid can have several rovers   *')
    print('* Each rover to be placed on the grid will need step 2 and step 3                         *')
    print('* If This is clear Press Enter to Start the Rover program                                 *') 
    print('*'*90)
  
  # Display the message for inputting the upper right coordinates
  def upper_right_msg(self):
    print('NB: The upper-right coordinate of the grid need two integers seperated by a single space')
    print('E.g: 5 5')

  # Display the message for rovers inputs
  def rover_msg(self):
    print('\nPlease provide rover\'s position and heading')
    print('NB: Heading can either be N,W,S or E')
    print('E.g: 1 2 N or 3 3 E')
  
  # Display message for the series of commands
  def command_msg(self):
    print('\nThe provide series of commands for the rover')
    print('NB: The commands can either be L R or M')
    print('E.g: LMLMLMLMM or MMRMMRMRRM')







