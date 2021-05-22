# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root):

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

        nodes_deque = collections.deque([root])
        direction = 1

        while nodes_deque:
            level_nodes = []
            for _ in range(len(nodes_deque)):
                cur_node = nodes_deque.popleft()
                level_nodes.append(cur_node.val)
                if cur_node.left:
                    nodes_deque.append(cur_node.left)
                if cur_node.right:
                    nodes_deque.append(cur_node.right)
            res.append(level_nodes[::direction])
            direction *= -1

        return res