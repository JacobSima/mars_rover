# Import Core or Third-party library
import pygame

# Import custome module
from db     import manager
db_manage = manager.Manager()

corner      = (5,5)
rovers_prev = [(2, 3, 'N'), (3, 4, 'N'), (3, 2, 'W'), (4, 3, 'W')]
rovers_curr = [(2, 3, 'N'), (3, 4, 'N'), (3, 2, 'W'), (4, 3, 'W')]


def get_rovers_prev():
  # Get rovers from db
  # rovers = db_manage.get_rovers()
  # return [ (rover[0]*100,rover[1]*100,rover[2]) for rover in rovers]
  return [ (rover[0]*100,rover[1]*100,rover[2]) for rover in rovers_prev]

def get_rovers_curr():
  # Get rovers from db
  # rovers = db_manage.get_rovers()
  # return [ (rover[0]*100,rover[1]*100,rover[2]) for rover in rovers]
  return [ (rover[0]*100,rover[1]*100,rover[2]) for rover in rovers_curr]

  


# Set graphic screen
# Make a grid ssystem of 50 hence, 1 would not allow a perfect display of the rover 
# grapgically
screen_width  = corner[0]*100
screen_height = corner[1]*100
screen  = pygame.display.set_mode((screen_width, screen_height))



# Load screen icon
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Title and icon
pygame.display.set_caption('Mars Rover Mission')

# Rover IMG
roverImg = pygame.image.load('rover.png')


# Draw rover on the screen
def rover_draw(rover):
  screen.blit(roverImg,(rover[0],rover[1]))






# Game Loop
running = True
while running:
  # Anything persistent in the window must be inside this loop
  screen.fill((15,82,186))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  # get the first rovers
  rovers = get_rovers()

  # draw the rovers
  for rover in rovers:
    rover_draw(rover)






  # to update any change you make to the screen
  pygame.display.update()










   
  

