# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, -float('inf'), float('inf'))
    
    def helper(self, node, lower_bound, upper_bound):
        if not node: return True
        if node.val >= upper_bound or node.val <= lower_bound:
            return False
        left = self.helper(node.left, lower_bound, node.val)
        right = self.helper(node.right, node.val, upper_bound)
        return left and right