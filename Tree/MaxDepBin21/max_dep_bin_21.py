# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
	def maxDepth(self, root: TreeNode):
		'''
		This function returns the max depth of root(a binary tree).

		Parameters
		------------------------
			root: TreeNode

		Returns
		------------------------
			max depth of root: int
		'''

		root = TreeNode(root)
		if not root:
			return 0
		if root and root.left is None and root.right is None:
			return 1
		return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
