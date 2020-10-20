import unittest
import max_area_island_18

class TestSolution(unittest.TestCase):

	def testMaxAreaOfIsland1(self):
		grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
				[0,0,0,0,0,0,0,1,1,1,0,0,0],
				[0,1,1,0,1,0,0,0,0,0,0,0,0],
				[0,1,0,0,1,1,0,0,1,0,1,0,0],
				[0,1,0,0,1,1,0,0,1,1,1,0,0],
				[0,0,0,0,0,0,0,0,0,0,1,0,0],
				[0,0,0,0,0,0,0,1,1,1,0,0,0],
				[0,0,0,0,0,0,0,1,1,0,0,0,0]]
		solution = max_area_island_18.Solution()
		result = solution.maxAreaOfIsland(grid)

		self.assertEqual(result, 6)


	def testMaxAreaOfIsland2(self):
		grid = [[0,0,0,0,0,0,0,0]]
		solution = max_area_island_18.Solution()
		result = solution.maxAreaOfIsland(grid)

		self.assertEqual(result, 0)

if __name__ == '__main__':
	unittest.main()