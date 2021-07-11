class Solution:
    def myPow(self, x, n):

        '''
        Parameters
        ----------
            x: float
            n: int
        Returns
        -------
            float
            ⇨ Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
        '''

        if n == 0:
            return 1
        # n が奇数のとき、
        if n % 2:
            return x * self.myPow(x, n - 1)
        # n が負(マイナス乗)のとき、
        if n < 0:
            return 1 / self.myPow(x, -n)

        return self.myPow(x * x, n/2)