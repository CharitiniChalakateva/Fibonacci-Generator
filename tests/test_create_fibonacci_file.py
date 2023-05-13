import unittest
from FibonacciGenerator import create_fibonacci_file

class TestCreateFibonacciFile(unittest.TestCase):
    def test_create_fibonacci_file(self):
        create_fibonacci_file(5)
        with open('fibonacci_5.txt', 'r') as f:
            content = f.readlines()
        content = [int(x.strip()) for x in content]
        self.assertEqual(content, [0, 1, 1, 2, 3, 5])

if __name__ == '__main__':
    unittest.main()
