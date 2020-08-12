import random
import turtle

# Returns a random color!
def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')
    
    # Make a new turtle
    dan=turtle.Turtle()
    # This code sets our shape to a turtle
    dan.shape('turtle')
    # Set your turtle's speed (0=fastest, 1=slowest, 10=faster)
    dan.speed(2)
    # Set your turtle's color using .color('green')
    dan.color('thistle')
    # Use a loop to repeat a the code below 50 times
    for i in range(50):
        # Set the turtle color to a random color
        dan.color(getRandomColor())
        # Move the turtle (5*i) pixels. 'i' is the loop variable
        dan.forward(5*i)
        # Turn the turtle (360/7) degrees to the right
        dan.right(360/7)
        # Change the turtle width to 'i' (the loop variable)
        dan.width(i)
        # Check the pattern against the picture in the recipe. If it matches, you are done!
    
# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
