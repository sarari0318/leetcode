
import unittest
import number_of_islands_17

class TestSolution(unittest.TestCase):

	def testNumIslands1(self):

		grid = [
		  ["1","1","1","1","0"],
		  ["1","1","0","1","0"],
		  ["1","1","0","0","0"],
		  ["0","0","0","0","0"]
		]

		solution = number_of_islands_17.Solution()
		result = solution.numIslands(grid)

		self.assertEqual(result, 1)


	def testNumIslands2(self):

		grid = [
		  ["1","1","0","0","0"],
		  ["1","1","0","0","0"],
		  ["0","0","1","0","0"],
		  ["0","0","0","1","1"]
		]

		solution = number_of_islands_17.Solution()
		result = solution.numIslands(grid)

		self.assertEqual(result, 3)


	def testNumIslands3(self):

		grid = [

		]

		solution = number_of_islands_17.Solution()
		result = solution.numIslands(grid)

		self.assertEqual(result, 0)


if __name__ == "__main__":
	unittest.main()
