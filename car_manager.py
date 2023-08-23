from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.level = 0
        self.car_speed = STARTING_MOVE_DISTANCE

    def create(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-245, 250))
            new_car.shapesize(1, 2)
            self.all_cars.append(new_car)

    def move_cars(self):
        self.car_speed = STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * self.level)
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.level += 1
        self.move_cars()

