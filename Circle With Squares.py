import turtle


def draw_square(some_turtle=None):
    for i in range(1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_art(josh=turtle):
    window = turtle.Screen()
    window.bgcolor("white")
    # Create the turtle Josh - Draws a Circle with Squares
    josh = turtle.Turtle()
    josh.shape("turtle")
    josh.color("red")
    josh.speed(5)

    for i in range(1, 37):
        draw_square(josh)
        josh.right(10)



    window.exitonclick()


draw_art()
