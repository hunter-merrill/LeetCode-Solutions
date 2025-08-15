# Post-order traverse, swapping right/left children upon returning to parent

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # Clever punny name explains functionality better than a comment ever could
        def postTreverse(parent):

            # Base case
            if not parent:
                return None

            # Traverse subtrees
            postTreverse(parent.left)
            postTreverse(parent.right)
            
            # Flip children ~pythonically~
            parent.left, parent.right = parent.right, parent.left

            return parent

        return postTreverse(root)