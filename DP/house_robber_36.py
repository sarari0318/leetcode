class Solution:
    def rob(self, nums):
        
        # rob or not at the N house(N=1, 2, 3 ,...)
        # ⇨ use Dynamic Programming
        
        house_num = len(nums)
        
        if house_num == 1:
            return nums[0]
        if house_num == 2:
            return max(nums[0], nums[1])
        
        dp = [0 for _ in range(house_num)]
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            # 2つ前までに盗んだ金銭と今の家の金銭の合計が、
            # 1つ前までに盗んだ金銭の合計より大きければ、2つ前までに盗んだ金銭と今の家の金銭の合計
            # 1つ前までに盗んだ金銭の合計より小さければ、１つ前までに盗んだ合計を
            # dp[i] として記録する
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]