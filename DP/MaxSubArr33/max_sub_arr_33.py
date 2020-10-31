from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        N = len(nums)
        dp = [0] * N

        dp[0] = nums[0]

        for i in range(1, N):
            subArr = max(dp[i-1], 0)
            dp[i] = subArr + nums[i]

        return max(dp)

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))