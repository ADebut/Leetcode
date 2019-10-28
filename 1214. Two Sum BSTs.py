# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        nodes = [(root1, root1.val)]
        r2 = root2
        while(nodes):
            node1, value1 = nodes.pop(0)
            root2 = r2
            queue = [(root2, root2.val)]
            while(queue):
                node2, value2 = queue.pop(0)
                if value2 > target - value1:
                    if node2.left:
                        queue.append((node2.left, node2.left.val))
                elif value2 < target - value1:
                    if node2.right:
                        queue.append((node2.right, node2.right.val))
                else:
                    return True
            if node1.right:
                nodes.append((node1.right, node1.right.val))
            if node1.left:
                nodes.append((node1.left, node1.left.val))
        return False