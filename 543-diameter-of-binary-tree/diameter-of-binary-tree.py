# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS
# Recurse per sub-tree
# --> base case: no children
# Keep track of depth
# Within loop, update nonlocal variable 'maxDiff'
# Return: maximum depth of any (grand)child

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        maxDiff = 0

        def dfs(node):
            nonlocal maxDiff

            # Base case (null)
            if not node:
                return 0

            maxDepthLeft = dfs(node.left) # Find max depth of left child subtree
            maxDepthRight = dfs(node.right) # Find max depth of right child subtree

            maxDiffLocal = maxDepthLeft + maxDepthRight
            if maxDiffLocal > maxDiff:
                maxDiff = maxDiffLocal
                
            return 1 + max(maxDepthLeft, maxDepthRight)
                
        dfs(root)
        return maxDiff