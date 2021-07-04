class Solution:
    def maxProfit(self, prices):

        '''
        Parameters
        ----------
            prices: List[int]
        Returns
        -------
            int
            ⇨ return the maximum profit we can achieve.
        '''
        
        days = len(prices)
        
        if days == 1:
            return 0
        
        # dp_buyには、それまで一番お得に買った時の値が入る
        # dp_sellには、それまで一番お得に売った時の値が入る
        dp_buy, dp_sell = [0 for _ in range(days)], [0 for _ in range(days)]
        
        dp_buy[0], dp_sell[0] = -prices[0], 0
        
        for i in range(1, len(prices)):
            # それまでで一番お得に売れた状態から i日目に買う
            # or それまでで一番お得に買えた時の、 より得な方をdp_buyに記録
            dp_buy[i] = max(dp_sell[i - 1] - prices[i], dp_buy[i - 1])
            # それまでで一番お得に買った状態から i日目に売る
            # or それまでで一番お得に売れた時の、 より得な法をdp_sellに記録
            dp_sell[i] = max(dp_buy[i - 1] + prices[i],  dp_sell[i - 1])
        
        return dp_sell[-1]