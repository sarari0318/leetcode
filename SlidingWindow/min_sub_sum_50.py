class Solution:
    def minSubArrayLen(self, target, nums):

        """
        Parameters
        ----------
            target: int
            nums: List[int]
        Returns
        -------
            int
        ⇨ return the minimal length of a contiguous subarray [numsl, numsl+1, ...,
          numsr-1, numsr] of which the sum is greater than or equal to target.
          If there is no such subarray, return 0 instead.
        """

        count = float('inf')
        total, start = 0, 0

        for i in range(len(nums)):
            total += nums[i]

            while total >= target:
                count = min(count, i - start + 1)
                total -= nums[start]
                start += 1

        return count if count != float('inf') else 0