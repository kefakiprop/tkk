import turtle

# Set up turtle
t = turtle.Turtle()
t.speed(0)

# Drawing a petal
def petal():
    for i in range(30):
        t.forward(1)
    t.right(2)

# Drawing a flower
def flower(size):
    for _ in range(6):
        petal()
        t.right(60)

# Function to draw an inner flower
def inner_flower():
    t.penup()
    t.goto(0, -50)  # Move the turtle to the center for the inner flower
    t.pendown()
    t.setheading(0)  # Reset heading to default
    t.color("red")  # You can change the color for the inner flower
    t.begin_fill()
    flower(5)  # Draw the inner flower (smaller size)
    t.end_fill()

# Drawing the outer flower
t.color("blue")  # Color for the outer flower
t.begin_fill()
flower(10)  # Draw the outer flower
t.end_fill()

# Draw the inner flower
inner_flower()

# Hide turtle and display the result
t.hideturtle()
turtle.done()
