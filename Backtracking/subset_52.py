class Solution:
    def subsets(self, nums):

        '''
         Parameters
        ----------
            nums: List[int] 
        Returns
        -------
            res: List[List[int]]
            ⇨ return all possible subsets (the power set).
        '''

        res = []
        self.backtracking(res, [], nums, 0)
        return res
        
    def backtracking(self, res, subset, nums, start):
        
        res.append(list(subset))

        # startからnumsの最後のindexまでの要素について線形探索
        for i in range(start, len(nums)):
            subset.append(nums[i])
            self.backtracking(res, subset, nums, i + 1)
            subset.pop()
