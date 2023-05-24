class FungeSpace:
    def __init__(self, file):
        lines = []
        self.width = 0
        self.height = 0
        self.code = []
        for line in file.readlines():
            lines.append(line)
            self.width = max(self.width, len(line))
            self.height += 1

        for line in lines:
            self.code.append(line + ' ' * (self.width - len(line)))

    def extend_space(self, x, y):
        self.width = max(x + 1, self.width)
        offset = self.width - len(self.code[0])
        for i in range(self.height):
            self.code[i] += ' ' * offset
        for i in range(self.height, x + 1):
            self.code.append(' ' * self.width)
        self.height = max(y + 1, self.height)

    def is_inside(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def __getitem__(self, index):
        x, y = index
        self.extend_space(x, y)
        return self.code[y][x]

    def __setitem__(self, index, value):
        if (type(value) != str) or len(value) != 1:
            raise ValueError("expected string of length 1, actual is", value)
        x, y = index
        self.extend_space(x, y)
        self.code[y] = self.code[y][:x] + value + self.code[y][x+1:]
