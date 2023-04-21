from pointer import Pointer


class Interpreter:
    def __init__(self, path):
        self.width = 0
        self.height = 0
        self.code = self.read_code_from_file(path)
        self.pointer = Pointer(self.width, self.height)


    def run(self):
        while self.pointer.is_inside():
            # TODO: finish later
            pass

    def read_code_from_file(self, path):
        with open(path) as file:
            result = []
            for line in file.readlines():
                result.append(line)
                self.height += 1
                self.width = max(self.width, len(line))
            return result
