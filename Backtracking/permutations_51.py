class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        '''
         Parameters
        ----------
            nums: List[int] 
        Returns
        -------
            res: List[List[int]]
            ⇨ return all the possible permutations.
        '''
        
        res = []
        # 既出の数字を記録
        seen = set()
        self.backtracking(res, [], seen, nums)
        return res
        
        
    def backtracking(self, res, sub_arr, seen, nums):

        if len(sub_arr) == len(nums):
            res.append(sub_arr)
        
        for i in range(len(nums)):
            # nums[i]が未出の数字の時
            if nums[i] not in seen:
                seen.add(nums[i])
                self.backtracking(res, sub_arr + [nums[i]], seen, nums)
                seen.remove(nums[i])
            