import unittest

def sum_of_even_numbers(nums):
    None

class SimpleTestCase(unittest.TestCase):
    def testA(self):
        assert sum_of_even_numbers([1, 0, 2]) == 2

    def testB(self):
        assert sum_of_even_numbers([5]) == None

    def testC(self):
        assert sum_of_even_numbers([5, 18, 18]) == 36

    def testD(self):
        assert sum_of_even_numbers([1, 2, 3, 4, '6']) == 6

    def testE(self):
        assert sum_of_even_numbers([1, '2', 3, 4, '6', 4]) == 8


if __name__ == "__main__":
    unittest.main()  # run all tests
