class Solution:
    def maxProfit(self, prices):

        '''
        Parameters
        ----------
            prices: List[int]
        Returns
        -------
            int
            ⇨ return the maximum profit you can achieve from this transaction. 
            If you cannot achieve any profit, return 0.
        '''
        
        days = len(prices)
        
        if days == 1:
            return 0
        
        dp_buy, dp_sell = [0 for _ in range(days)], [0 for _ in range(days)]
        
        dp_buy[0], dp_sell[0] = -prices[0], 0
        
        # 最終日に買うことは無いので、days - 1
        for i in range(1, days - 1):
            dp_buy[i] = max(dp_buy[i - 1], -prices[i])

        for j in range(1, days):
            dp_sell[j] = max(dp_buy[j - 1] + prices[j], dp_sell[j - 1])
            
        return dp_sell[-1]