from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.start()
        self.reach_end = False

    def move(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.reach_end = True

        self.forward(MOVE_DISTANCE)

    def start(self):
        self.goto(STARTING_POSITION)
        self.reach_end = False

