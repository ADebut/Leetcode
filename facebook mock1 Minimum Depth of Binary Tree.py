# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        nodes = [(root, 0)]
        ans = 2 ** 31 - 1
        while nodes:
            node, depth = nodes.pop(0)
            if not node:
                continue
            if node and (node.left or node.right):
                nodes.append((node.left, depth + 1))
                nodes.append((node.right, depth + 1))
            else:
                ans = min(ans, depth + 1)
        return ans