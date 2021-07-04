class Solution:
    def maxSubArray(self, nums):

        '''
        Parameters
        ----------
            nums: List[int]
        Returns
        -------
            int
            ⇨ find the contiguous subarray (containing at least one number) 
            which has the largest sum and return its sum.
        '''

        N = len(nums)
        
        if N == 1:
            return nums[0]
        
        dp = [0 for _ in range(N)]
        dp[0] = nums[0]
        
        for i in range(1, N):
            dp[i] = nums[i] + max(0, dp[i-1])
            
        return max(dp)