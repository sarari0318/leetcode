# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        if not preorder or not inorder:
            return None
        
        node_val = preorder.pop(0)
        node_index = inorder.index(node_val)
        
        root = TreeNode(node_val)
        root.left = self.buildTree(preorder, inorder[:node_index])
        root.right = self.buildTree(preorder, inorder[node_index + 1:])
        
        return root