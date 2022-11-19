import unittest

def second_highest_number(nums):
    None

class SimpleTestCase(unittest.TestCase):
    def testA(self):
        assert second_highest_number([1, 0, 2]) == 1

    def testB(self):
        assert second_highest_number([5]) == null

    def testC(self):
        assert second_highest_number([5, 46597384]) == 46597384

    def testD(self):
        assert second_highest_number([1, 2, 3, 4, '6']) == 2

    def testE(self):
        assert second_highest_number([1, '2', 3, 4, '6']) == 3

        # def testF(self):
        # print(highest_number([-1,'2',-3, '6', '!']))
        # assert highest_number([-1,'2',-3, '6', '!']) == 6


if __name__ == "__main__":
    unittest.main()  # run all tests