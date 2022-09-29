from random import randint

class Race:
    def __init__(self, name):
        self.name = name
        self.speed = None
        self.winner = False
    
    def move_car(self):
        speed = randint(170, 181)
        self.speed = speed
        print(f"{self.name} is moving at {speed} kmph. \n")
        
    def declare_winner(cars):
        speeds = [{'car_name': car.name, 'car_speed': car.speed} for car in cars]
        speeds.sort(key=lambda self: self["car_speed"])
        winner = speeds[len(speeds) - 1] 
        print(f"AND THE WINNER IS {winner['car_name']}!!!")

cars_names = ["4Runner", "Corolla", "F2", "Hilux", "Mazda", "BMW"]
cars = []
for car_name in cars_names:
    car = Race(car_name)
    car.move_car()
    cars.append(car) 

Race.declare_winner(cars)