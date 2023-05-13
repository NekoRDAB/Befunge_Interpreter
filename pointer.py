class Pointer:
    def __init__(self, width, height):
        self._x = 0
        self._y = 0
        self._width = width
        self._height = height
        self._direction = (1, 0)

    def is_inside(self):
        return 0 <= self._x < self._width and 0 <= self._y < self._height

    def get_position(self):
        return self._x, self._y

    def change_direction(self, new_direction):
        self._direction = new_direction

    def move(self):
        self._x = (self._x + self._direction[0]) % self._width
        self._y = (self._y + self._direction[1]) % self._height
