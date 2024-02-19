import turtle

# Define a function to draw a pattern using turtle graphics
def draw_turtel():

    # Set up the drawing window with a black background
    window = turtle.Screen()
    window.bgcolor("black")

    # Create a turtle named amin, set its color to orange, and shape to 'turtle'
    amin = turtle.Turtle()
    amin.color("orange")
    amin.shape("turtle")

    # Draw a complex pattern using a loop
    for i in range(36):
        # Move the turtle forward and rotate it to create a part of the pattern
        amin.forward(100)
        amin.left(30)
        amin.forward(100)
        # Change the turtle's color to white and draw a circle
        amin.color("white")
        amin.circle(20)
        # Change the turtle's color back to orange
        amin.color("orange")
        # Continue drawing the pattern with specific movements and rotations
        amin.left(150)
        amin.forward(100)
        amin.left(30)
        amin.forward(100)
        amin.left(160)
    # Position the turtle to end the drawing
    amin.right(90)
    amin.forward(300)
    # Wait for a user click to close the window
    window.exitonclick()

# Call the function to execute the drawing
draw_turtel()
