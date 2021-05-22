# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):

        '''
        Parameters
        ------------------------
            root: TreeNode
        Returns
        ------------------------
            res: List[List[int]]

        '''

        res = []

        if not root:
            return res

        deque_node = collections.deque([root])

        while deque_node:
            level_nodes = []
            for i in range(len(deque_node)):
                curNode = deque_node.popleft()
                level_nodes.append(curNode.val)
                if curNode.left:
                    deque_node.append(curNode.left)
                if curNode.right:
                    deque_node.append(curNode.right)

            res.append(level_nodes)

        return res
