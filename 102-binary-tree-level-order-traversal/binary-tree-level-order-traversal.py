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

        def bfs(node):
            nonlocal dq

            # Add children (if they exist)
            for node in [node.left, node.right]:
                if node:
                    dq.append(node)
        
        levels = []
        while dq:
            
            # Run through nods in current level (= node in queue when level starts)
            levels.append([])
            for i in range(len(dq)):
                currNode = dq.popleft()
                levels[-1].append(currNode.val)
                bfs(currNode)
        
        return levels