"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root == None:
            return 0
        # Depth level of the tree
        depth = 0
        
        # Loops through children array
        for child in root.children:
            # Compares current depth of depth with a new level of depth 
            # Sets the biggest value to variable depth
            depth = max(depth, self.maxDepth(child))
        
        # As going deeper into the tree increases depth by 1
        return depth + 1 