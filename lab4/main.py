# Spencer Hoffman
# Lab 4
# August 4 - Sunday

# Imports the turtle graphics module
import turtle
import sys

# creates a turtle (pen) an sets the speed (where 0 is fastest and 10 is slowest)
# The colors can be set through their names or through hexadecimal codes, use hex for accuracy
turtle.screensize(200, 200, bg="#FFFFFF")
myPen = turtle.Turtle()
myPen.color("#800000")
myPen.speed(100000)
# If you would like to slow down the animation, uncomment the next line. Higher delay, the slower it will be
#turtle.delay(100)
# setting out box sizes to the n sq pixels per box
boxSize = 10


# myPen.setheading(n) points pen to given angle direction.
# where n queals the angle (think unit circle).
# 0 points to the right, 90 to go up, 180 to go to the left 270 to go down

# Positions myPen in top left area of the screen
# This canvas is currently set to 200*200 pixels or a 20x20 box of 10 sq pixels each
def goto_origin(myPen):
    myPen.home()

# This function draws a box by drawing each side of the square and using the fill function
def box(intDim):
    # for loop to draw boxes
    myPen.begin_fill()
    for i in range(4):
        #moves the pen forward and then rotates 90 degrees
        myPen.forward(intDim)
        myPen.left(90)
    #rotated 360 and moved forward 4 times
    #make box
    myPen.end_fill()

# Here is an example of how to draw a box using the box function
# Comment these two lines out when you draw your own images
# box(boxSize)
# turtle.done()


# Challenge functions (2 bonus pts each)
# def save_image(): # saves the screen to an image/vector file
# You have a function for boxes, can you make functions for circles and triangles?
# def circle(intRadius):
# def triangle(intLength): #This can be an equilateral triangle, or not

#*************************************************************************************************************
# ------These are the instructions on how to move "myPen" around after drawing a box.--------
# penup() lifts the pen so it doesn't draw anything and can be moved freely
# pendown() puts the pen down and it draws as it moves, e.g.:
# myPen.penup()
# myPen.forward(boxSize)
# myPen.pendown()
#****************************************************************************************************

# You will save your drawings in text files, which you will read from the art folder.
# You have two sample art pieces already saved. The first line will be a list of colors, and the
# rest of the lines will be rows of pixels, which you should read and save as a list of lists.

#***************************************************
# This first list stores the color values, e.g.:
# #FFFFFF,#FFFF00,#000000,#61380B,#F4FA58
#********************************************************

# The drawings are stored using a "list of lists" structure where each value within every list
# element is the index of the color in the pallet list for that pixel

# This function will take in a filename path and load the art piece stored in that file.
# You are to parse the art into two lists, one for the color palette (first line of file),
# and a second with the pixel values (list of lists).
# The function returns both lists
def load_art(path):
    list_of_lists = []
    pallet = []
    with open(path, 'r') as artfile:
        artfile = artfile.read().splitlines()
        for line in range(len(artfile)):
            if line == 0:
                pallet = artfile[line].split(",")
            else:
                list_of_lists.append(artfile[line].split(','))
    return pallet, list_of_lists
# This function takes a pallet and pixel list (matrix) to draw the picture
# You are to write this function
def draw(pallet, pixels):
    for row in pixels:
        for pixel in row:
            int_pixel = int(pixel)
            box_color = pallet[int_pixel]
            myPen.color(box_color)
            box(boxSize)
            myPen.forward(boxSize)
        myPen.right(90)
        myPen.forward(boxSize)
        myPen.right(90)
        myPen.forward(len(row)*10)
        myPen.right(180)


# Should give the user a list of the possible drawing pieces you have and ask which one to draw
# After drawing the piece, ask the if they would like to draw a different piece until they quit the program.
if __name__ == '__main__':
    # sample for loading art and calling draw
    ##pallet_1, pixels_1 = load_art('art/mario.txt')
    choice = int(input("Choose File:\n [1] Banana\n [2] Mario\n [3] Pacman Ghost\n [4] Smile\n [5] Space Invader\n [6] Mushroom\n [7] Man\n [8] Pacman\n [Q] To Quit\n:"))
    if choice == 1:
            pallet_1, pixels_1 = load_art('art/banana.txt')
    if choice == 2:
            pallet_1, pixels_1 = load_art('art/mario.txt')
    if choice == 3:
            pallet_1, pixels_1 = load_art('art/ghost.txt')
    if choice == 4:
            pallet_1, pixels_1 = load_art('art/smile.txt')
    if choice == 5:
            pallet_1, pixels_1 = load_art('art/invader.txt')
    if choice == 6:
            pallet_1, pixels_1 = load_art('art/mushroom.txt')
    if choice == "Q":
            sys.exit(0)
    if choice == 7:
            pallet_1, pixels_1 = load_art('art/man.txt')
    if choice == 8:
            pallet_1, pixels_1 = load_art('art/pacman.txt')
    turtle.tracer(10)
    draw(pallet_1, pixels_1)
    # You need this to prevent the window from closing after drawing
    turtle.done()
