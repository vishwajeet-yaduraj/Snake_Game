from turtle import Turtle

positions = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.boxes = []
        self.create_snake()
        self.head = self.boxes[0]

    def create_snake(self):
        for p in positions:
            self.create_box(p)

    def create_box(self, p):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(p)
        self.boxes.append(new_turtle)

    def extend(self):
        self.create_box(self.boxes[-1].position())

    def move(self):
        for box in range(len(self.boxes) - 1, 0, -1):
            x = self.boxes[box - 1].xcor()
            y = self.boxes[box - 1].ycor()
            self.boxes[box].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
