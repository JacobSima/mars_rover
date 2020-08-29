# Import Core or Third-party library
import time


def quiting(val,quitter):
  text = 'exits' if quitter else 'will continue'
  
  if quitter:
    print('***** Thank You for using Mars Rover program ******\n')
    print(f'Application {text} in {val} seconds')
    time.sleep(val)
    quit()
  else:
    print(f'Application {text} in {val} seconds')
    time.sleep(val)
    return