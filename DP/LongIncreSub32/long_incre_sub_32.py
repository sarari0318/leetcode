from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        if not nums:
            return 0

        N = len(nums)
        dp = [1] * N

        # [10,9,2,5,3,7,101,18]
        # [1,1,1,2,2,1,1,1]

        # linear scan from left to right
        for i in range(1, N):
            count = 0
            for j in range(0, i):
                if nums[j] < nums[i]:
                    count = max(count, dp[j])
            dp[i] = 1 + count

        return max(dp)

if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLIS([10,9,2,5,3,7,101,18]))