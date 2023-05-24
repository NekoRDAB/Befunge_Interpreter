import unittest
from interpreter import Interpreter

PATH = r"test_files/example_file.befunge"


class Test(unittest.TestCase):
    def test_cardinal_moving(self):
        interpreter = Interpreter()
        interpreter.create_space(PATH)

        for i in range(17):
            interpreter.pointer.move()
        self.assertEqual((0, 0), interpreter.pointer.get_position())

        interpreter.execute_given_instruction("v")
        for i in range(4):
            interpreter.pointer.move()
        self.assertEqual((0, 0), interpreter.pointer.get_position())

        interpreter.execute_given_instruction("^")
        interpreter.pointer.move()
        self.assertEqual((0, 3), interpreter.pointer.get_position())

        interpreter.execute_given_instruction("<")
        interpreter.pointer.move()
        self.assertEqual((16, 3), interpreter.pointer.get_position())

    def test_flying(self):
        interpreter = Interpreter()
        interpreter.create_space(PATH)

        interpreter.pointer.change_direction((2, 1))
        interpreter.pointer.set_position(1, 1)
        for i in range(3):
            interpreter.pointer.move()
        self.assertEqual((1, 1), interpreter.pointer.get_position())


if __name__ == "main":
    unittest.main()
