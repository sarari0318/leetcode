class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        求められている答え
        ⇨ 回転したsorted listであるnumsの中から、targetのindexを求める
        
        ① [1,2,3,4,5] 完全なソート
        ② [2,3,4,5,1] ソートが左半分に偏る
        ③ [4,5,1,2,3] ソートが右半分に偏る
        '''
        
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # ①, ② に関して
            if nums[left] <= nums[mid]:
                # ① に関して
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                # ② に関して
                else:
                    left = mid + 1
            # ③ に関して
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return -1