from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        dq = deque([root])
        currLevel = 1 # Nodes in current level
        nextLevel = 0 # Nodes in next level (incremented as we go)

        def bfs(node):
            nonlocal dq, currLevel, nextLevel

            # Add children (if they exist)
            for node in [node.left, node.right]:
                if node:
                    dq.append(node)
                    nextLevel += 1
        
        levels = [[]]
        while dq:
            
            # Check if next level reached
            if currLevel == 0:
                currLevel = nextLevel # Move on to next level
                nextLevel = 0 # Reset nodes in next level
                levels.append([]) # Prepare list in which to add new children

            currNode = dq.popleft() # Get oldest node in queue
            levels[-1].append(currNode.val) # Add it to the current level
            bfs(currNode) # Find its children
            currLevel -= 1 # Decrease remaining nodes in level
        
        return levels