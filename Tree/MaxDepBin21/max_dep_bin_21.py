class Solution:
	def maxDepth(self, root):
		root = TreeNode(root)
		print(root.left)
		if not root:
			return 0
		if root and root.left is None and root.right is None:
			return 1
		return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))