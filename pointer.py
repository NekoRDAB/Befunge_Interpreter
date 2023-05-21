class Pointer:
    def __init__(self, width, height):
        self._x = 0
        self._y = 0
        self._width = width
        self._height = height
        self._delta = (1, 0)

    def is_inside(self):
        return 0 <= self._x < self._width and 0 <= self._y < self._height

    def get_position(self):
        return self._x, self._y

    def change_direction(self, new_direction):
        self._delta = new_direction

    def move(self, s):
        self._x = (self._x + s * self._delta[0]) % self._width
        self._y = (self._y + s * self._delta[1]) % self._height
