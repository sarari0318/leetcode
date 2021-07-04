class Solution:
    def uniquePaths(self, m: int, n: int):

        '''
        Parameters
        ----------
            m: int
            n: int
        Returns
        -------
            int
            ⇨ return the num of possible unique paths of a m x n grid.
        '''

        dp = [0] * n
        dp[0] = 1

        for _ in range(m):
            for col in range(1, n):
                dp[col] += dp[col-1]

        return dp[-1]