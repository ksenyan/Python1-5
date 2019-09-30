import turtle
import random
colourType = input("Would you like to choose your colours or \
make it random each time? (Type 'me' or 'random': ")
print ("Have fun drawing! Once you're done, just make your line length 0.")
colours = ("red", "orange", "yellow", "green", "turquoise", "cyan", "blue",\
           "purple", "indigo", "gold", "maroon", "violet", "magenta", "navy",\
           "skyblue", "lightgreen", "darkgreen","chocolate", "brown", "black", "gray")
length = 1
while length != '0':
    if colourType.lower() == "me" : 
        penColour = input ("Choose a colour! ")
        penSize = input ("Choose a pen size! ")
        angle  = input ("Choose an angle! ")
        length = input ("Choose a line length! ")
        turtle.pencolor(penColour)
        turtle.pensize (int(penSize))
        turtle.right (int(angle))
        turtle.forward (int(length))
    else :
        penColour = (random.choice(colours))
        penSize = input ("Choose a pen size! ")
        angle  = input ("Choose an angle! ")
        length = input ("Choose a line length! ")
        turtle.pencolor(penColour)
        turtle.pensize (int(penSize))
        turtle.right (int(angle))
        turtle.forward (int(length))

print ("Thanks for drawing!")
turtle.bye()

