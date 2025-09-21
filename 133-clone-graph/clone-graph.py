from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# Traverse graph and build adjacency list
# Return adjacencies of node 1

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        visited = {node: Node(node.val)}
        dq = deque([node])

        # Create new nodes and link them to their original counterparts
        while dq:
            
            nodeOld = dq.popleft()
            
            for nb in nodeOld.neighbors:
                if nb not in visited:
                    visited[nb] = Node(nb.val) # Mark visited, linking old neighbor to new
                    dq.append(nb)
                visited[nodeOld].neighbors.append(visited[nb]) # Connect new node to new neighor

        return visited[node] # Return new version of node 1