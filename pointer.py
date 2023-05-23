class Pointer:
    def __init__(self, interpreter):
        self._x = 0
        self._y = 0
        self.interpreter = interpreter
        self._delta = (1, 0)

    def get_position(self):
        return self._x, self._y

    def change_direction(self, new_direction):
        self._delta = new_direction

    def move(self, s=1):
        self._x = self._x + s * self._delta[0]
        self._y = self._y + s * self._delta[1]
        if self.is_out_of_space(self._x, self._y):
            self.wrap()

    def wrap(self):
        self.revert()
        dx, dy = self._delta
        x, y = self._x, self._y
        while not self.is_out_of_space(x + dx, y + dy):
            self.move()
        self.revert()

    def get_pos(self, add_delta=False):
        if add_delta:
            dx, dy = self._delta
            return dx + self._x, dy + self._y
        return self._x, self._y

    def rotate(self, direction=1):
        dx, dy = self._delta
        new_delta = (direction * dy, direction * dx)
        self._delta = new_delta

    def get_next_dest(self):
        delta = self._delta
        dx, dy = self._delta
        return self._x + dx, self._y + dy

    def is_out_of_space(self, x, y):
        interpreter = self.interpreter
        return 0 <= x < interpreter.width and 0 <= y < interpreter.height

    def revert(self):
        dx, dy = self._delta
        self._delta = (-dx, -dy)
