import unittest
import word_ladder_20

class TestSolution(unittest.TestCase):

	def testLadderLength1(self):
		beginWord = "hit",
		endWord = "cog",
		wordList = ["hot","dot","dog","lot","log","cog"]

		solution = word_ladder_20.Solution()
		result = solution.ladderLength(beginWord, endWord, wordList)

		self.assertEqual(result, 5)

	def testLadderLength2(self):
		beginWord = "hit"
		endWord = "cog"
		wordList = ["hot","dot","dog","lot","log"]

		solution = word_ladder_20.Solution()
		result = solution.ladderLength(beginWord, endWord, wordList)

		self.assertEqual(result, 0)

if __name__ == '__main__':
	unittest.main()