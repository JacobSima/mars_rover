# MARS ROVER CHALLENGE

## 1. Details of Challenge

### 1a. Description: 

A squad of robotic rovers are to be landed by NASA on a plateau on Mars. This plateau, which is curiously rectangular, must be navigated by the rovers so that their on board cameras can get a complete view of the surrounding terrain to send back to Earth.

A rover’s position is represented by a combination of an x and y co-ordinates and a letter representing one of the four cardinal compass points. The plateau is divided up into a grid to simplify navigation. An example position might be
`0, 0, N` , which means the rover is in the bottom left corner and facing North.

In order to control a rover, NASA sends a simple string of letters. The possible letters are `L` , `R` and `M` . `L` and `R` makes the rover spin 90 degrees left or right respectively, without moving from its current spot. `M` means move forward one grid
point, and maintain the same heading. Assume that the square directly North from `(x,y)` is `(x,y+1)`.

### 1b. Input:

The problem below requires some kind of input. You are free to implement any mechanism for feeding input into your solution.

The first line of input is the upper-right coordinates of the plateau, the lower-left coordinates are assumed to be `(0,0)` . The rest of the input is information pertaining to the rovers that have been deployed. Each rover has two lines of input. The first line gives the rover’s position, and the second line is a series of instructions telling the rover how to explore the plateau.

The position is made up of two integers and a letter separated by spaces, corresponding to the x and y co-ordinates and the rover’s orientation. Each rover will be finished sequentially, which means that the second rover won’t start to move until the first one has finished moving.


### 1c. Output:

The output for each rover should be its final co-ordinates and heading.


### 1d. Example of input and output

Test Input:

`5 5`

`1 2 N`

`LMLMLMLMM`

`3 3 E`

`MMRMMRMRRM`

Expected Output:

`1 3 N`

`5 1 E`

## 2. Code Overview

### 2a. A modular approach. 

The project is built in very modular approach, which can help to expand the project or make future modifcation without any trouble within the project. This README file describe few details of the modular files and ruuning sequences. which are kind of bonus to better understand the flow of this program

## 3. Folders and modules 

The project file contents two module folders,`db` and `lib` 


###   3a. db

The directory consists of two python scripts'file, which are data.py and manager.py
the data.py serves as the database of this program, all the value entered from the user will be save in this data.py file

The manager.py is where most of our logics done, this is where critical operatios of the program is done and hold most of the main logic.

###   3b. lib

The directory consists of three files, alert.py,input.py and msg_screen.py

alert.py file provide few line of code that allow the program to have nice alert while placing rovers on the plateau

msg_screen.py, is where most of the message that are displayed on the command are written. We made this modular so that,there is only one place to deal with all the printing message of the screen.

input.py, the file get all the input enterred from the user and do a proper validation before using them.
input validation was added in this program to avoid the program to fail in case user enter wrong value however, alert and warning messages are printed on the command line, to notify the user where they did wrong and what are the chance to quit the code for the lack of following proper instructions

## 4. How to run the code and tests 

### 4a. Running the code

#### 4a. 1 Clone this project

#### 4a. 2 Run requirement.txt file
From your command line run : `pip install requirements.txt` to install all the dependancies of this program

#### 4a. 3 Run main.py
main.py is the main entry file of the project. By running or executing this file via a command line, all the instructions will be display accordingly and very clear
We simply execute from command line: `python main.py` 


## 5. General comments and future tests

- the goal of this project was reached, nevertheless we were not able to do extras work on the TCP, telnet and graphic interface. We tried pygame for the interface but could not get the proper logic and be able to run both script in a thread from main.py while creating a new console. this was an issue, but in future this matter can be resolved

- The project was quite fun and challenging, but finally the end result is a success.
