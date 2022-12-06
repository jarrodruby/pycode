import unittest

def remove_non_integers(nums):
    filtered = filter(lambda num: isinstance(num, int), nums)
    return list(filtered)

def sort_list_of_integers(nums):
    return sorted(nums)

def second_last_element_of_list(nums):
    return nums[len(nums) - 2]

def second_highest_number(nums):
    if len(nums) < 2:
        return None

    nums = remove_non_integers(nums)
    nums = sort_list_of_integers(nums)
    result = second_last_element_of_list(nums)
    return result

class SimpleTestCase(unittest.TestCase):
    # 1.
    #### remove_non_integers ####
    def test_remove_non_integers_1(self):
        assert remove_non_integers([1, 0, 2]) == [1, 0, 2]

    def test_remove_non_integers_2(self):
        assert remove_non_integers([1, 'a', 0, 2]) == [1, 0, 2]

    # 2.
    #### sort_list_of_integers ####
    def test_sort_list_of_integers_1(self):
        assert sort_list_of_integers([1, 0, 2]) == [0, 1, 2]

    def test_sort_list_of_integers_2(self):
        assert sort_list_of_integers([11, 0, -2]) == [-2, 0, 11]

    # 3.
    #### second_last_element_of_list ####
    def test_second_last_element_of_list_1(self):
        result = second_last_element_of_list([0, 1, 2, 3, 8, 55])
        assert result == 8

    def test_second_last_element_of_list_2(self):
        result = second_last_element_of_list([11, 11, 33])
        assert result == 11

    # 4.
    #### second_highest_number ####
    def test_second_highest_number_1(self):
        result = second_highest_number([1, 0, 2])
        assert result == 1

    def test_second_highest_number_2(self):
        assert second_highest_number([5]) == None

    def test_second_highest_number_3(self):
        result = second_highest_number([46597384, 46597385])
        assert result == 46597384

    def test_second_highest_number_4(self):
        result = second_highest_number([1, 2, 3, 4, '6'])
        assert result == 3

    def test_second_highest_number_5(self):
        result = second_highest_number([1, '2', 3, 4, '6'])
        print(result)
        assert result == 3


if __name__ == "__main__":
    unittest.main()
