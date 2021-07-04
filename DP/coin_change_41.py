class Solution:
    def coinChange(self, coins, amount):

        '''
        Parameters
        ----------
            coins: List[int]
            amount: int
        Returns
        -------
            int
            ⇨ return the fewest number of coins that you need to make up that amount.
            If that amount of money cannot be made up by any combination of the coins, return -1.
        '''
        
        if amount == 0:
            return 0
        
        dp = [0] + [float('inf') for _ in range(amount)]
        
        for coin in coins:
            for i in range(len(dp)):
                if i >= coin:
                    # i - coin、つまり iとcoin１枚の差額分までのコイン使用最低枚数
                    # + コイン１枚分
                    dp[i] = min(dp[i - coin] + 1, dp[i])
                    
        return dp[-1] if dp[-1] != float('inf') else -1