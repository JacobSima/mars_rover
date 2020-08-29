# Import Core or Third-party library
import os,sys 

# import Custom library
from alert    import quiting
from db       import data, manager
    
                                                                       

# Input Validation
class InputValidator():

  def __init__(self):
    pass

  # Validate Enter key
  def enter_Key_validate(self,ent_key):
    
    return True if ent_key == '' else False
  
  # Validate the Upper-right coordonate of the grid
  def corner_validate(self,coordi):
    try:
      coordi = tuple([int(val) for val in coordi[0].strip().split(' ') if val != ' '])
      if len(coordi) <= 1:
        return False,coordi
      else:
        return True,coordi
    except:
      return False,coordi
  
  # validate Rover position
  def rover_pos_validate(self,rover):
    init_val = [val for val in rover[0].strip().split()]
    if len(init_val) != 3:
      print('Too less or Much arguments provided.')
      return False,rover

    try:
      position = tuple([int(val) for val in init_val[0:2] if val != ' '])
      return True, position
    except :
      print('Position values are not integers')
      return False,rover
    

  # validate Rover heading
  def rover_str_validate(self,rover):
    try:
      heading = [val for val in rover[0].strip().split()][-1].upper()
      if heading not in data.Headings.keys():
        print('Heading is not a valid cardinal compass point abbreviation ')
        return False,rover  
      return True, heading
    except:
      return False,rover
  
  # Validate Rover command
  def rover_cmd_validate(self,command):
    cmd_str = data.Commands
    result = ''
    for letter in command:
      if letter in cmd_str:
        result = True
      else:
        result  = False
        print('\nWrong series command enterred')
        break
    return result, command



    




# Input Text Enterred
class InputText():
  # Initiate the InputValidator
  validate = InputValidator()
  db_man   = manager.Manager()

  def __init__(self):
    pass

  # Enter key Pressed Input
  def enter_key_pressed(self):
    looping  = 0
    chance   = 3
    while looping < 3:
      print('')
      ent_key = input('Press Enter to Start the Program \n')
      valid    = InputText.validate.enter_Key_validate(ent_key)
      if not valid :
        looping += 1
        chance  -= 1
        s = 's' if chance > 1 else ''
        print('Please Press only Enter, not other key,')
        print(f'You left with {chance} chance{s} to try press only Enter')
      else:
        os.system('clear')
        break
      
      # Exist the program in case user not following the instructions
      if looping == 3:
        print('\n Start the script again, You failed to follow the instruction')
        quiting(2,True)

  
  # Get the upper-right coordinate from User
  def get_upper_right_coord(self):
    looping = 0
    chance  = 3
    coordi  = []
    while looping < 3 :
      corner  = input('\nEnter upper-right coordinate of the grid\n')
      coordi.append(corner)
      valid,point = InputText.validate.corner_validate(coordi)
      if not valid:
        coordi  = []
        looping += 1
        chance  -= 1
        s = 's' if chance > 1 else ''
        print('Corner has to be a (int,int) values')
        print(f'You left with {chance} chance{s} left')
        
        # Update the DB
        self.db_man.set_corner('') 

      else:
        # Update the DB
        self.db_man.set_corner(point)
        break

      # Exist the program in case user not following the instructions
      if looping == 3:
        print('\n Start the script again, You failed to follow the instruction')
        quiting(2,True)

  # Get rover's position and heading
  def get_rover_position(self):
    looping = 0
    chance  = 3
    rover   = []
    while looping < 3:
      pos   = input('\nEnter Rover position  and heading\n')
      rover.append(pos)
      valid_int,position = InputText.validate.rover_pos_validate(rover) 
      valid_str,heading = InputText.validate.rover_str_validate(rover)
      if not valid_int or not valid_str:
        looping += 1
        chance  -= 1
        rover   = []
        s = 's' if chance > 1 else ''
        print('Rover is in this format (int,int,str)')
        print(f'You left with {chance} chance{s} left')

      else:
        # Update DB
        if self.db_man.add_rover(position,heading):
          looping = 0
          chance  = 3
          rover   = []
          print('Rover succeffully added into the Mars Mission')
          break
        else:
          looping += 1
          chance  -= 1
          rover   = []
          s = 's' if chance > 1 else ''
          print(f'You left with {chance} chance{s} left')
        
             
      # Exist the program in case user not following the instructions
      if looping == 3:
        print('\n Start the script again, You failed to follow the instruction')
        quiting(2,True)
  
  # Get rovers commands
  def get_commands(self):
    looping   = 0
    chance    = 3
    while looping < 3 :
      command        = input('\nPlease Enter command for the rover\n').upper()
      valid,command  = InputText.validate.rover_cmd_validate(command)
      if not valid :
        looping += 1
        chance  -= 1
        s = 's' if chance > 1 else ''
        print(f'You left with {chance} chance{s} left')
      else:
        # Update the DB
        data.commands.append(command)
        looping   = 0
        chance    = 3
        break
      
      # Exist the program in case user not following the instructions
      if looping == 3:
        print('\n Start the script again, You failed to follow the instruction')
        quiting(2,True)



  # Get User approval if continue adding rovers or get the final positions
  def user_appv(self):
    while True:
      # Ask the user to enter more rovers or continue
      print(' ')
      print('You have at least added rovers but if You like,you can still')
      print('to add more rovers to the Mars Plateau ')
      print('Or You can press Enter to View the rovers\' positions')
      print(' ')
      print('Press Y or y to Enter more rovers ')
      print('Press N or n to get final positions\n')
      resp    = input(' ')
      if resp == 'Y' or resp == 'y':
        self.get_rover_position()
        self.get_commands()
      elif resp == 'N' or resp == 'n':
        break
      else:
        print('Please select correct Option')
    


        

       
        


        


        

      
        

      
      






    
    
    




      

      
        
