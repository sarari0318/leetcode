class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtracking(res, [], nums, 0)
        return res
        
    def backtracking(self, res, subset, nums, start):
        
        res.append(list(subset))
        for i in range(start, len(nums)):
            subset.append(nums[i])
            self.backtracking(res, subset, nums, i + 1)
            subset.pop()
