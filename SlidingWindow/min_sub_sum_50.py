class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        count = float('inf')
        total, start = 0, 0
        
        for i in range(len(nums)):
            total += nums[i]
            
            while total >= target:
                count = min(count, i - start + 1)
                total -= nums[start]
                start += 1
                
        return count if count != float('inf') else 0