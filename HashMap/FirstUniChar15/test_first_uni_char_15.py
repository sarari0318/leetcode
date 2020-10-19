import unittest
import first_uni_char_15

class TestSolution(unittest.TestCase):
    def testFirstUniqChar1(self):
        s = ""
        solution = first_uni_char_15.Solution()
        result = solution.firstUniqChar(s)
        self.assertEqual(result, -1)


    def testFirstUniqChar2(self):
        s = None
        solution = first_uni_char_15.Solution()
        result = solution.firstUniqChar(s)
        self.assertEqual(result, -1)


    def testFirstUniqChar3(self):
        s = "leetcode"
        solution = first_uni_char_15.Solution()
        result = solution.firstUniqChar(s)
        self.assertEqual(result, 0)

if __name__ == "__main__":
	unittest.main()