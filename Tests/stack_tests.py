import unittest
from interpreter import Interpreter


class Test(unittest.TestCase):
    def test_stack_empty(self):
        interpreter = Interpreter()
        self.assertEqual([], interpreter.stack)

    def test_stack_contains_numbers(self):
        interpreter = Interpreter()
        expected_stack = []
        for i in range(10):
            interpreter.execute_given_instruction(str(i))
            expected_stack.append(i)
        self.assertEqual(expected_stack, interpreter.stack)

    def test_push_pop(self):
        interpreter = Interpreter()
        expected_stack = [1]
        instructions = ["1", "2", "3", "$", "$"]
        for instruction in instructions:
            interpreter.execute_given_instruction(instruction)
        self.assertEqual(expected_stack, interpreter.stack)

    def test_operations(self):
        interpreter = Interpreter()
        instructions = ["2", "3", "2", "1", "+", "*", "/"]
        expected_stack = [4]
        for instruction in instructions:
            interpreter.execute_given_instruction(instruction)
        self.assertEqual(expected_stack, interpreter.stack)


if __name__ == "__main__":
    unittest.main()
