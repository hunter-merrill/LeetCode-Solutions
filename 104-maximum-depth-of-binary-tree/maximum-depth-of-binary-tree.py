# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS
# Keep track of max depth by taking max(dfs left child, dfs right child) 
#   and returning 1 extra each time

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):

            # base case: null (i.e. parent has no child here)
            if not node:
                return 0

            return 1 + max(dfs(node.left), dfs(node.right))
        
        return dfs(root)