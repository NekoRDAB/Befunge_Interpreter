class Pointer:
    def __init__(self, width, height):
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height

    def is_inside(self):
        return 0 <= self.x < self.width and 0 <= self.y < self.height
