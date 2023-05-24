import unittest
from funge_space import FungeSpace


PATH_TO_FILE = (r"C:\Users\Professional\Desktop\python_files"
                r"\pythonProject\Befunge_Interpreter"
                r"\Tests\befunge98_tests\test_files\example_file.befunge")
WIDTH = 17
HEIGHT = 4


class Test(unittest.TestCase):
    def test_init(self):
        with open(PATH_TO_FILE) as file:
            space = FungeSpace(file)
            self.assertEqual((WIDTH, HEIGHT), (space.width, space.height))

    def test_in_space_get(self):
        with open(PATH_TO_FILE) as file:
            space = FungeSpace(file)
            self.assertEqual('>', space[0, 0])
            self.assertEqual('l', space[5, 1])
            self.assertEqual(' ', space[16, 3])
            self.assertEqual((WIDTH, HEIGHT), (space.width, space.height))

    def test_out_of_space_get(self):
        with open(PATH_TO_FILE) as file:
            space = FungeSpace(file)
            self.assertEqual(' ', space[17, 0])
            self.assertEqual((18, HEIGHT), (space.width, space.height))
            self.assertEqual(' ', space[150, 150])
            self.assertEqual((151, 151), (space.width, space.height))

    def test_in_space_set(self):
        with open(PATH_TO_FILE) as file:
            space = FungeSpace(file)
            space[0, 0] = 'D'
            space[16, 3] = '%'
            self.assertEqual('D', space[0, 0])
            self.assertEqual('%', space[16, 3])

    def test_out_of_space_set(self):
        with open(PATH_TO_FILE) as file:
            space = FungeSpace(file)
            space[17, 4] = "D"
            self.assertEqual('D', space[17, 4])
            self.assertEqual((18, 5), (space.width, space.height))
            space[150, 150] = "Y"
            self.assertEqual('Y', space[150, 150])
            self.assertEqual((151, 151), (space.width, space.height))


if __name__ == "__main__":
    unittest.main()
