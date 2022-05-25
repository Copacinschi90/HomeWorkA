class Rocket():

    def __init__(self):
        # Each rocket has an (x,y) position.
        self.x = 0
        self.y = 0

    def move_up(self):

        self.y += 1

    def move_right(self):
        self.x += 1

    def move_down(self):
        self.y += 1

    def move_left(self):
        self.y += 1

    def current_position(self):
        curent_position

my_rocket = Rocket()
print("current_postion:", my_rocket)

my_rocket.move_right()
print("current_position:", my_rocket)

my_rocket.move_right()
print("current_position:", my_rocket)