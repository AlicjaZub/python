from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.coordinates = []

    def create_car(self):
        random_chance = randint(1,6)
        if random_chance == 1:
            car = Turtle("square")
            car.penup()
            car.shapesize(1.5, 3)
            car.color(choice(COLORS))
            car.goto(self.generate_position())
            self.all_cars.append(car)
         
    def generate_position(self):
        y = choice(range(-240, 280, 40))
        
        if y in self.coordinates:
            self.coordinates.append(y)
            return (280 + 105 * self.coordinates.count(y), y)
        else:
            self.coordinates.append(y)
            return (280, y)

    def move_cars(self, level):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE + ((level -1) * MOVE_INCREMENT))
            if car.xcor() < -320:
                self.coordinates.remove(int(car.ycor()))
                car.hideturtle()
                self.all_cars.remove(car)
        