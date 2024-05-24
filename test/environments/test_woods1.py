import unittest

from src.environments.woods1 import Woods1


class TestWoods1Methods(unittest.TestCase):

    def test_init(self):
        woods1 = Woods1('data/woods1.txt')
        self.assertIsNotNone(woods1)


if __name__ == '__main__':
    unittest.main()
