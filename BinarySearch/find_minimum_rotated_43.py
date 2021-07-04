class Solution:
    def findMin(self, nums):
        
        '''
        Parameters
        ----------
            nums: List[int]
        Returns
        -------
            int
            ⇨ return the minimum element of the given array.
        
        ① [1,2,3,4,5] 完全なソート
        ② [4,5,1,2,3] [5,1,2,3,4] ソートが右半分に偏る
        ③ [3,4,5,1,2] [2,3,4,5,1] ソートが左半分に偏る
        '''
        
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            # ②に対応する条件
            if nums[mid] < nums[right]:
                right = mid
            # ③に対応する条件
            elif nums[mid] > nums[right]:
                left = mid + 1
        return nums[left]