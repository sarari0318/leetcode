class Solution:
    def subarraySum(self, nums, k):

        '''
        Parameters
        ----------
            nums: List[int]
            k: int
        Returns
        -------
            int
            ⇨ return the total number of continuous subarrays whose sum equals to k.
        '''
        # count: 合計がkとなるパターン数を記録
        # total: numを足し合わせていったものを記録
        count, total = 0, 0
        sumdict = {0:1}
        
        for num in nums:
            total += num
            
            if total - k in sumdict.keys():
                count += sumdict[total - k]
                
            if total in sumdict.keys():
                sumdict[total] += 1
            else:
                sumdict[total] = 1
            
        return count