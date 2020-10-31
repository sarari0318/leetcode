import unittest
import uni_path_34

class TestSolution(unittest.TestCase):



    def testUniquePaths1(self):
        m, n = 3, 7
        test_solution = uni_path_34.Solution()
        result = test_solution.uniquePaths(m, n)
        self.assertEqual(result, 28)

    def testUniquePaths2(self):
        m, n = 3, 0
        test_solution = uni_path_34.Solution()
        result = test_solution.uniquePaths(m, n)
        self.assertEqual(result, 0)

    def testUniquePaths3(self):
        m, n = 0, 2
        test_solution = uni_path_34.Solution()
        result = test_solution.uniquePaths(m, n)
        self.assertEqual(result, 0)

if __name__ == "__main__":
    unittest.main()