import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Smiling Emoji")

# Create a turtle for drawing
emoji_turtle = turtle.Turtle()
emoji_turtle.speed(2)  # Set the drawing speed


# Draw a smiling emoji
def draw_smiling_emoji():
    # Draw the face
    emoji_turtle.color("yellow")
    emoji_turtle.begin_fill()
    emoji_turtle.circle(100)
    emoji_turtle.end_fill()

    # Draw the left eye
    emoji_turtle.penup()
    emoji_turtle.goto(-40, 120)
    emoji_turtle.pendown()
    emoji_turtle.color("black")
    emoji_turtle.begin_fill()
    emoji_turtle.circle(15)
    emoji_turtle.end_fill()

    # Draw the right eye
    emoji_turtle.penup()
    emoji_turtle.goto(40, 120)
    emoji_turtle.pendown()
    emoji_turtle.color("black")
    emoji_turtle.begin_fill()
    emoji_turtle.circle(15)
    emoji_turtle.end_fill()

    # Draw the smiling mouth
    emoji_turtle.penup()
    emoji_turtle.goto(-40, 70)
    emoji_turtle.pendown()
    emoji_turtle.color("black")
    emoji_turtle.width(5)
    emoji_turtle.right(90)
    emoji_turtle.circle(40, 180)


# Draw the smiling emoji
draw_smiling_emoji()

# Close the turtle graphics window when clicked
screen.exitonclick()
