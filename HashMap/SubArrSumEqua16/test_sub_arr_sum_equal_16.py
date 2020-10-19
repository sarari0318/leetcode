import unittest
import sub_arr_sum_equal_16

class TestSolution(unittest.TestCase):

	def testSubarraySum1(self):

		nums = [1, 2, 3, 5]
		k = 5

		solution = sub_arr_sum_equal_16.Solution()
		result = solution.subarraySum(nums, k)

		self.assertEqual(result, 2)


	def testSubarraySum2(self):

		nums = []
		k = 5

		solution = sub_arr_sum_equal_16.Solution()
		result = solution.subarraySum(nums, k)

		self.assertEqual(result, 0)

if __name__ == "__main__":
	unittest.main()