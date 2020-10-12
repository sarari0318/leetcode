class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # return a list including the numbers' indexes which the total is target
        # pre: nums:list, target:int
        # post: list
        
        # step0: use hashmap
        dict = {}
        
        # step1: linear scan from left to right and forcus on the indexes
        for i in range(len(nums)):
            if nums[i] not in dict.keys():
                dict[target-nums[i]] = i
            else:
                return [dict[nums[i]], i]
            
        # testcase: nums[2, 7, 11, 15], target=9
        # nums[0] = 2 ⇨ dict[9-2]=dict[7]=0 ⇨ dict{7:0}
        # nums[1] = 7 ⇨ 7 in dict.keys() ⇨ return [0, 1]