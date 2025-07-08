import turtle
from math import cos, sin

# Create the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(10)

# Create the sun
sun = turtle.Turtle()
sun.shape('circle')
sun.color('yellow')

# Define the Planet class
class Planet(turtle.Turtle):
    def __init__(self, name, radius, color):  # Corrected __init__ method
        super().__init__(shape='circle')
        self.name = name
        self.radius = radius
        self.c = color
        self.color(self.c)
        self.up()
        self.angle = 0.0  # Initialize angle as a float
        self.label = turtle.Turtle()  # Create label turtle
        self.label.hideturtle()
        self.label.up()
        self.label.color("white")

    def move(self):
        # Calculate the position
        x = self.radius * cos(self.angle)
        y = self.radius * sin(self.angle)
        self.goto(sun.xcor() + x, sun.ycor() + y)

        # Update the label's position and text
        self.label.goto(self.xcor() + 10, self.ycor() + 10)
        self.label.clear()
        self.label.write(self.name, align="center", font=("Arial", 10, "normal"))

# Create planets
mercury = Planet("Mercury", 40, 'grey')
venus = Planet("Venus", 80, 'orange')
earth = Planet("Earth", 100, 'blue')
mars = Planet("Mars", 150, 'red')
jupiter = Planet("Jupiter", 180, 'brown')
saturn = Planet("Saturn", 230, 'pink')
uranus = Planet("Uranus", 250, 'light blue')
neptune = Planet("Neptune", 280, 'purple')

# Add planets to a list
myList = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

# Function to update positions
def update_positions():
    screen.update()
    for planet in myList:
        planet.move()

    # Increment each planet's angle
    mercury.angle += 0.05
    venus.angle += 0.03
    earth.angle += 0.01 
    mars.angle += 0.007
    jupiter.angle += 0.002
    saturn.angle += 0.0018
    uranus.angle += 0.0016
    neptune.angle += 0.001

    # Call the function again after 50ms
    screen.ontimer(update_positions, 50)

# Start the animation
update_positions()

# Keep the window open
turtle.mainloop()
