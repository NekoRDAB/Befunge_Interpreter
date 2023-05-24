import unittest
from interpreter import Interpreter

PATH = r"C:\Users\Professional\Desktop\python_files" \
       r"\pythonProject\Befunge_Interpreter\Tests\test_files" \
       r"\example_file.befunge"


class Test(unittest.TestCase):
    def test_direction_straight_move_instruction(self):
        interpreter = Interpreter()
        interpreter.create_space(PATH)
        instructions = ["<"]
        for instruction in instructions:
            interpreter.execute_given_instruction(instruction)
        self.assertEqual((-1, 0), interpreter.pointer._delta)

    def test_coordinates_straight_move_instruction(self):
        interpreter = Interpreter()
        interpreter.create_space(PATH)
        instructions = ["<"]
        for instruction in instructions:
            interpreter.execute_given_instruction(instruction)
        interpreter.pointer.move()
        self.assertEqual(
            (interpreter.space.width - 1, 0),
            (interpreter.pointer._x, interpreter.pointer._y))

    def test_direction_conditional_move_instruction(self):
        interpreter = Interpreter()
        interpreter.create_space(PATH)
        instructions = ["1", "_"]
        for instruction in instructions:
            interpreter.execute_given_instruction(instruction)
        self.assertEqual((-1, 0), interpreter.pointer._delta)

    def test_coordinates_conditional_move_instruction(self):
        interpreter = Interpreter()
        interpreter.create_space(PATH)
        instructions = ["1", "_"]
        for instruction in instructions:
            interpreter.execute_given_instruction(instruction)
        interpreter.pointer.move()
        self.assertEqual(
            (interpreter.space.width - 1, 0),
            (interpreter.pointer._x, interpreter.pointer._y))


if __name__ == "main":
    unittest.main()
