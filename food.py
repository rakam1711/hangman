# snake_game_python
from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=1.5, stretch_wid=1.5)
        self.color('blue')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        x_axis = random.randint(-280, 280)
        y_axis = random.randint(-280, 280)
        self.goto(x_axis, y_axis)



