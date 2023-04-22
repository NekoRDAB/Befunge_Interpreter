import unittest
from main import path_correct


PATH_TO_DIR = (r"C:\Users\Professional\Desktop\python_files"
               r"\pythonProject\Befunge_Interpreter\Tests\test_files"
               "\\")


class Test(unittest.TestCase):
    def test_correct_file(self):
        path = PATH_TO_DIR + "example_file.befunge"
        self.assertTrue(path_correct(path))

    def test_file_not_found(self):
        path = PATH_TO_DIR + "not_existing_file"
        self.assertFalse(path_correct(path))

    def test_incorrect_extension(self):
        path = PATH_TO_DIR + "incorrect_extension.txt"
        self.assertFalse(path_correct(path))


if __name__ == "__main__":
    unittest.main()
