class Solution:
    def minDepth(self, root: TreeNode) -> int:

        if not root:
            return 0

        if root and root.left is None and root.right is None:
            return 1

        if root.left and not root.right:
            return 1 + self.minDepth(root.left)

        if not root.left and root.right:
            return 1 + self.minDepth(root.right)

        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))