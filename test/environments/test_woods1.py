import random
import unittest

from src.environments.woods1 import Woods1


class TestWoods1Methods(unittest.TestCase):

    def test_init(self):
        woods1 = Woods1('data/woods1.txt')
        self.assertIsNotNone(woods1)
        height = woods1.get_height()
        width = woods1.get_width()
        rand_height = random.randint(0, height - 1)
        rand_width = random.randint(0, width - 1)
        woods1.set_current_position([rand_height, rand_width])


if __name__ == '__main__':
    unittest.main()
