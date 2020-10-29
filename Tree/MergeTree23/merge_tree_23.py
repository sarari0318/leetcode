class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:

        if t1 is None and t2 is None:
            return None

        if t1:
            v1, l1, r1 = t1.val, t1.left, t1.right
        else:
            v1, l1, r1 = 0, None, None

        if t2:
            v2, l2, r2 = t2.val, t2.left, t2.right
        else:
            v2, l2, r2 = 0, None, None

        root = TreeNode(v1+v2)
        root.left = self.mergeTrees(l1, l2)
        root.right = self.mergeTrees(r1, r2)

        return root