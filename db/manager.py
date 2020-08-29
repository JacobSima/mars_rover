# Import core or third-party libraries
import os

# Import Custom module
from db  import data

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
      
    os.system('clear')
    print(output)


  # Get rover
  def get_commands(self):
    commands = data.commands
    return commands
  

  # Set rovers
  def set_rovers(self,x,y,heading):
    data.rovers.append(tuple((x,y,heading)))
  

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
          rover = self.rotate_l(rover,i)

        if serie == 'R':
          rover = self.rotate_r(rover,i)

        if serie == 'M':
          rover,cnt = self.move_rover(rover,i)
          
          # if the rover cannot be move, then break the loop to check next rover
          if not cnt :
            break



  








  





  












# manger = Manager()
# print(manger.get_rovers())

  # Get Single rover
  # def get_single_rover(self,id):

  #   try:
  #     rover_id = int(id)
  #     if len(data.rovers) > 0 and rover_id <= len(data.rovers) :
  #       rover    = data.rovers[rover_id]
  #       position = (rover[0],rover[1])   # (x,y)
  #       heading  = rover[2]    # N
  #       return position, heading
  #     else:
  #       raise Exception('IndexError or rovers list Empty')    
  #   except :
  #     raise Exception ('The Id not an integer value or rovers length not evaluable')



    

        






