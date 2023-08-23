import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

create_a_car = 0
car_manager = []
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
score_board = Scoreboard()
car = CarManager()

score_board.write_score()

screen.listen()
screen.onkeypress(player.move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    # increase car speed
    if player.reach_end:
        score_board.write_score()
        player.start()
        car.increase_speed()

    # create a car
    car.create()

    # Detect collision with cars
    for car_in_list in car.all_cars:
        if car_in_list.distance(player) < 20:
            score_board.game_over()
            game_is_on = False
    car.move_cars()
    screen.update()

screen.exitonclick()
