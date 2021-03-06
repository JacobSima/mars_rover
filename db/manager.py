# Import Core or Third-party library
import time,os

# Import Custom module
from db   import data
from lib  import alert 

# Manger your Rover right here
class Manager():

  def __init__(self):
    pass


  # Get the grid coordinate
  def get_corner(self):
    return data.corner
    

  # set the grid coordinate
  def set_corner(self,point):
    data.corner = point
  

  # Get rover
  def get_rovers(self):
    rovers = data.rovers
    return rovers
  
  # get final rovers and print them
  def get_rov_final(self):

    output = ''
    rovers = data.rovers
    for rover in rovers:
      output += '%d %d %s\n' % (rover[0], rover[1], rover[2]) 
      
    # Clean the screen, just like typing clear on CMD
    os.system('clear')
    print(output)


  # Get rover
  def get_commands(self):
    commands = data.commands
    return commands
  

  # Set rovers
  def set_rovers(self,x,y,heading):
    data.rovers.append(tuple((x,y,heading)))
  
  # Set Image base on the heading
  def set_img(self,heading):
    if heading == 'E':
      data.imgs.append('img/E_R.png')
    if heading == 'N':
      data.imgs.append('img/N_R.png')
    if heading == 'W':
      data.imgs.append('img/W_R.png')
    if heading == 'S':
      data.imgs.append('img/S_R.png') 
  

  # Check rover inside the grid
  # (x,y)
  # return False = not within the grid
  # return True  = within the grid
  def rover_in_grid(self,position):   

    x,y  = (position[0],position[1])
    Xmax =  self.get_corner()[0]
    Ymax =  self.get_corner()[1]
    return True if ((0 <= x <= Xmax) and (0 <= y <= Ymax)) else False 


  # Check if available position in the grid for the rover
  # (x,y)
  # return False = not available
  # return True  = available
  def check_available_position(self,position):  

    in_rover  = (position[0],position[1])
    rovers = data.rovers 
    return False if in_rover in [rover for rover in [(r[0],r[1]) for r in rovers]] else True
  

  # Check if a given rover position is already taken on the grid
  # (x,y)
  def check_position(self,position):  
    # get false means not available
    if not self.check_available_position(position): 
      print(str(position),' Is already taken on the grid')   
      return False
    
    # get false means not within the plateau
    if not self.rover_in_grid(position):
      print(str(position),'Outside the grid')
      return False

    return True

  
  # Add rover to the plateau
  def add_rover(self,position,heading):        
    rover_pos = (position[0],position[1])
    if self.check_position(rover_pos):
      self.set_rovers(position[0],position[1],heading)
      self.set_img(heading)
      return True
    else:
      return False
  
  # Update rover position in the plateau
  def update_rover(self,rover,rover_id):
    data.rovers[rover_id] = rover


  # Rotate Rover Left
  def rotate_l(self,rover,rover_id):
    heading     = rover[2]
    new_heading = ''
    # Do the rotation
    if heading == 'E':
      new_heading = 'N'
    if heading == 'N':
      new_heading = 'W'
    if heading == 'W':
      new_heading = 'S'
    if heading == 'S':
      new_heading = 'E'
    # Set the the heading
    updated_rover = (rover[0],rover[1],new_heading)

    # Update Rover in the plateau
    self.update_rover(updated_rover,rover_id)
    return updated_rover


  # Rotate Rover Right
  def rotate_r(self,rover,rover_id):
    heading     = rover[2]
    new_heading = ''
    # Do the rotation
    if heading == 'E':
      new_heading = 'S'
    if heading == 'S':
      new_heading = 'W'
    if heading == 'W':
      new_heading = 'N'
    if heading == 'N':
      new_heading = 'E'
    # Set the the heading
    updated_rover = (rover[0],rover[1],new_heading)

    # Update Rover in the plateau
    self.update_rover(updated_rover,rover_id)
    return updated_rover
    
  
  # Move the rover
  def move_rover(self,rover,rover_id):

    heading     = rover[2]
    x           = rover[0]
    y           = rover[1]

    # Move
    if heading == 'E':
      x = x + 1
    if heading == 'S':
      y = y - 1
    if heading == 'W':
      x = x - 1
    if heading == 'N':
      y = y + 1
    
    updated_rover = (x,y,heading)
    position = (x,y)
    if self.check_position(position):
      # Update Rover in the plateau
      self.update_rover(updated_rover,rover_id)
      print('Rover is moving to this coordinates',updated_rover)
      time.sleep(data.command_delay)
      print('Rover movement completed')
      return updated_rover,True
    else:
      print('Move can not be executed for this rover: ',updated_rover)
      return rover, False

  
  # Run commands
  def run_commands(self):
    rovers   = self.get_rovers()
    commands = self.get_commands()
    # The most tricky part, this rover return value is very important
    for i,(rover,command) in enumerate(zip(rovers,commands)):     
      for serie in command:
        if serie == 'L':
          print(rover,' is getting rotated to the left...')
          rover = self.rotate_l(rover,i)         
          time.sleep(data.command_delay)
          print(rover,' Rotation completed')

        if serie == 'R':
          print(rover,' is getting rotated to the right...')
          rover = self.rotate_r(rover,i)
          time.sleep(data.command_delay)
          print(rover,' Rotation completed')

        if serie == 'M':
          rover,cnt = self.move_rover(rover,i)       
          # if the rover cannot be move, then break the loop to check next rover
          if not cnt :
            break
  
  def continue_rover_code(self):
    
    # Run command of series
    self.run_commands()

    # Print out the result
    self.get_rov_final()

    # Quit the program
    # alert.quiting(5,True)


  








  





  








    

        






