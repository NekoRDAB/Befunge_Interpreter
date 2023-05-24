class Pointer:
    def __init__(self, interpreter):
        self._x = 0
        self._y = 0
        self.interpreter = interpreter
        self._delta = (1, 0)

    def get_position(self):
        return self._x, self._y

    def set_position(self, x, y):
        self._x = x
        self._y = y

    def change_direction(self, new_direction):
        self._delta = new_direction

    def move(self, s=1):
        self._x = self._x + s * self._delta[0]
        self._y = self._y + s * self._delta[1]
        space = self.interpreter.space
        if not space.is_inside(self._x, self._y):
            self.wrap()

    def wrap(self):
        self.revert()
        dx, dy = self._delta
        space = self.interpreter.space
        while space.is_inside(self._x + dx, self._y + dy):
            self._x += dx
            self._y += dy
        self.revert()

    def rotate(self, direction=1):
        dx, dy = self._delta
        new_delta = (direction * dy, direction * dx)
        self._delta = new_delta

    def get_next_dest(self):
        dx, dy = self._delta
        return self._x + dx, self._y + dy

    def is_inside(self):
        interpreter = self.interpreter
        return interpreter.space.is_inside(self._x, self._y)

    def revert(self):
        dx, dy = self._delta
        self._delta = (-dx, -dy)
