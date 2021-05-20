# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums):

    	'''
		Parameters
	    ------------------------
	        nums: List[int]
	    Returns
	    ------------------------
	        root: TreeNode

    	'''


        if not nums:
            return None

        mid_idx = len(nums) // 2

        root = TreeNode(nums[mid_idx])
        root.left = self.sortedArrayToBST(nums[:mid_idx])
        root.right = self.sortedArrayToBST(nums[mid_idx + 1:])

        return root