# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Start at root
# DFS: Search children recursively
# At left child, check if value < biggest value in search
# At right child, check if value > smallest value in search
# In either case, if not true, abort; otherwise, recur on children
#
# Recursive case: children
# Base case: no children

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(node: TreeNode, smallest: int, biggest: int) -> bool:

            # Base case: child is None
            if not node:
                return True

            # Recursive case
            if smallest < node.val < biggest:
                return dfs(node.left, smallest, node.val) and dfs(node.right, node.val, biggest)
            else:
                return False
        
        inf = sys.maxsize
        return dfs(root, -inf, inf)