import unittest
import paint_fence_31

class TestSolution(unittest.TestCase):
	def testNumWays1(self):
		n = 0
		k = 3
		solution = paint_fence_31.Solution()

		result = solution.numWays(n, k)
		self.assertEqual(result, 0)


	def testNumWays2(self):
		n = 1
		k = 3
		solution = paint_fence_31.Solution()

		result = solution.numWays(n, k)
		self.assertEqual(result, 3)


	def testNumWays3(self):
		n = 2
		k = 3
		solution = paint_fence_31.Solution()

		result = solution.numWays(n, k)
		self.assertEqual(result, 9)


	def testNumWays4(self):
		n = 3
		k = 2
		solution = paint_fence_31.Solution()

		result = solution.numWays(n, k)
		self.assertEqual(result, 6)


if __name__ == "__main__":
	unittest.main()
