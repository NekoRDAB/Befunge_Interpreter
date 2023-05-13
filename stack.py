class Stack:
    def __init__(self):
        self.list = []

    def pop(self):
        if len(self.list) > 0:
            return self.list.pop(-1)
        return 0

    def push(self, value):
        self.list.append(value)

    def peek(self):
        if len(self.list) > 0:
            return self.list[-1]
        return 0

    def count(self):
        return len(self.list)
