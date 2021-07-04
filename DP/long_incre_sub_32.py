class Solution:
    def lengthOfLIS(self, nums):

        '''
        Parameters
        ----------
            nums: List[int]
        Returns
        -------
            int
            ⇨ return the length of the longest strictly increasing subsequence.
        '''
        
        N = len(nums)
        dp = [1] * N


        for i in range(1, N):
            count = 0
            # i番目より前の要素をチェック
            for j in range(0, i):
                if nums[j] < nums[i]:
                    count = max(count, dp[j])
            dp[i] = 1 + count

        return max(dp)