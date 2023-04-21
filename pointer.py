class Pointer:
    def __init__(self, width, height):
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
        self.direction = None

    def is_inside(self):
        return 0 <= self.x < self.width and 0 <= self.y < self.height

    def get_position(self):
        return self.x, self.y

    def change_direction(self, ):

    def move(self):