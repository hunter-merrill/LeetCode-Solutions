# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # DFS, keep track of depth
        # When leaf reached, cascade back up, comparing left/right subtree depths at each node
        
        balanced = True
        def dfs(node):

            # Traverse left and right, then compare heights
            lDepth, rDepth = 0, 0
            if node.left:
                lDepth += dfs(node.left)
            if node.right:
                rDepth += dfs(node.right)

            # Verify that difference is within bounds of balance
            if abs(lDepth - rDepth) > 1:
                nonlocal balanced 
                balanced = False
            
            # Increment depth count
            return 1 + max(lDepth, rDepth)
        
        if root:
            dfs(root)
        return balanced