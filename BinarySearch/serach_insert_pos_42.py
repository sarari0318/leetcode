class Solution:
    def searchInsert(self, nums, target):

        '''
        Parameters
        ----------
            nums: List[int]
            target: int 
        Returns
        -------
            int
            ⇨ return the index where it would be if it were inserted in order.
        '''
        
        # 左端のindexをleft, 右端のindexをrightとする
        left, right = 0, len(nums) - 1
        
        while left <= right:
            # mid: leftとrightの中間のindex
            mid = (left + right) // 2
            # nums[mid]がtargetと等しければ、midを返す
            if nums[mid] == target:
                return mid
            # nums[mid]がtargetより大きければ、
            # この後は左半分だけを見れば良いので、rightをmid - 1に移動
            elif nums[mid] > target:
                right = mid - 1
            # nums[mid]がtargetより小さければ、
            # この後は右半分だけを見れば良いので、leftをmid + 1に移動
            else:
                left = mid + 1
                
        return left