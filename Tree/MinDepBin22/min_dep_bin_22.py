# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        '''
        This function returns the min depth of root(a binary tree).

        Parameters
        ------------------------
            root: TreeNode

        Returns
        ------------------------
            min depth of root: int

        '''

        if not root:
            return 0
        if root and root.left is None and root.right is None:
            return 1
        # if there is only left
        if root.left and not root.right:
            # validate only left
            return 1 + self.minDepth(root.left)
        # if there is only right
        if not root.left and root.right:
            # validate only right
            return 1 + self.minDepth(root.right)

        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))