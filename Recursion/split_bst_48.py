class Solution(object):
    def splitBST(self, root, v):

        """
        Parameters
        ----------
            root: TreeNode
            v: int
        Returns
        -------
            TreeNode
        ⇨ return the root TreeNode of both subtrees after splitting, in any order.
        """

        if not root:
            return [None, None]
        if root.val == v:
            temp = root.right
            root.right = None
            return [root, temp]
        elif root.val > v:
            small, large = self.splitBST(root.left, v)
            root.left = large
            return [small, root]
        else:
            small, large = self.splitBST(root.right, v)
            root.right = small
            return [root, large]