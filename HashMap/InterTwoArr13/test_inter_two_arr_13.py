import unittest
import inter_two_arr_13

class TestSolution(unittest.TestCase):
    def test_intersection(self):

        test_nums1 = [1,2,2,1]
        test_nums2 = [2,2]

        test_solution = inter_two_arr_13.Solution()
        result = test_solution.intersection(test_nums1, test_nums2)
        self.assertEqual(result, [2])


    def test_intersection2(self):

        test_nums1 = [4,9,5]
        test_nums2 = [9,4,9,8,4]

        test_solution = inter_two_arr_13.Solution()
        result = test_solution.intersection(test_nums1, test_nums2)
        self.assertEqual(result, [9, 4])

    def test_intersection3(self):

        test_nums1 = []
        test_nums2 = [9,4,9,8,4]

        test_solution = inter_two_arr_13.Solution()
        result = test_solution.intersection(test_nums1, test_nums2)
        self.assertEqual(result, [])

    def test_intersection4(self):

        test_nums1 = []
        test_nums2 = []

        test_solution = inter_two_arr_13.Solution()
        result = test_solution.intersection(test_nums1, test_nums2)
        self.assertEqual(result, [])

unittest.main()