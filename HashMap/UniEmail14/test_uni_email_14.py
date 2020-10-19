import unittest
import uni_email_14

class TestSolution(unittest.TestCase):
    def testNumUniqueEmails(self):

        test_emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
        test_solution = uni_email_14.Solution()
        result = test_solution.numUniqueEmails(test_emails)
        self.assertEqual(result, 2)


    def testNumUniqueEmails2(self):

        test_emails = []
        test_solution = uni_email_14.Solution()
        result = test_solution.numUniqueEmails(test_emails)
        self.assertEqual(result, 0)

unittest.main()