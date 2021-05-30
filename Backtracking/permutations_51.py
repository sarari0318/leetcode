class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        seen = set()
        self.backtracking(res, [], seen, nums)
        return res
        
        
    def backtracking(self, res, sub_arr, seen, nums):
        if len(sub_arr) == len(nums):
            res.append(sub_arr)
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
                self.backtracking(res, sub_arr + [nums[i]], seen, nums)
                seen.remove(nums[i])
            