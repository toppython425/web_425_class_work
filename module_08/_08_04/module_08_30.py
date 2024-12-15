import time


class Tracks:
    def change_direction(self, left, on):
        print('tracks: ', left, on)


class Wheels:
    def change_direction(self, left, on):
        print('wheels: ', left, on)


class Vehicle:
    def __init__(self, controller):
        self.controller = controller

    def turn(self, left):
        self.controller.change_direction(left, True)
        time.sleep(2.0)
        self.controller.change_direction(left, False)


tracked = Vehicle(Tracks())
wheeled = Vehicle(Wheels())
tracked.turn(True)
wheeled.turn(False)
