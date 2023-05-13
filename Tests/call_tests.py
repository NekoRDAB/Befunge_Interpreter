import unittest
from interpreter import Interpreter

PATH = r"C:\Users\Professional\Desktop\python_files" \
       r"\pythonProject\Befunge_Interpreter\Tests\test_files" \
       r"\example_file.befunge"


class Test(unittest.TestCase):
    def test_get_call(self):
        interpreter = Interpreter()
        interpreter.read_code_from_file(PATH)
        instructions = ["1", "2", "g"]
        for instruction in instructions:
            interpreter.execute_given_instruction(instruction)
        self.assertEqual(ord(":"), interpreter.stack.peek())

    def test_get_call_negative_coordinates(self):
        interpreter = Interpreter()
        interpreter.read_code_from_file(PATH)
        instructions = ["1", "-", "0", "2", "-", "g"]
        for instruction in instructions:
            interpreter.execute_given_instruction(instruction)
        self.assertEqual(0, interpreter.stack.peek())

    def test_put_call(self):
        interpreter = Interpreter()
        interpreter.read_code_from_file(PATH)
        instructions = ["2", "1", "2", "p"]
        for instruction in instructions:
            interpreter.execute_given_instruction(instruction)
        self.assertEqual(chr(2), interpreter.code[2][1])


if __name__ == "main":
    unittest.main()