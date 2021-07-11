class Solution:
    def kthGrammar(self, n, k):

        '''
        Parameters
        ----------
            n: int
            k: int
        Returns
        -------
            int
            ⇨ return the kth (1-indexed) symbol in the nth row of a table of n rows.

        ex) Input: n = 3, k = 1
            row 1: 0
            row 2: 01
            row 3: 0110
            ⇨ Output: 0
        '''

        if n == 1:
            return 0

        else:
            # kが偶数のとき
            if k % 2 == 0:
                # even index of current level is opposite of parent level's [(K+1)//2]
                return 0 if self.kthGrammar(n - 1, (k + 1) // 2) else 1
            # kが奇数のとき
            else:
                # odd index of current level is the same as parent level's [(K+1)//2]
                return 1 if self.kthGrammar(n - 1, (k + 1) // 2) else 0

        return int(res)