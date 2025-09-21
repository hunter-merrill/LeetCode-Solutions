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

        visited = set([node])
        adjOld = {} # Adjacency lists for old graph
        oldToNew= {} # Dict of old nodes: respective new node
        dq = deque([node])

        # Create new nodes and link them to their original counterparts
        while dq:
            
            nodeOld = dq.popleft()
            nodeNew = Node(nodeOld.val, [])
            oldToNew[nodeOld] = nodeNew

            #adjOld[nodeOld] = []
            for nb in nodeOld.neighbors:
                #adjOld[nodeOld].append(nb)
                if nb not in visited:
                    dq.append(nb)
                    visited.add(nb)

        # For every old node, add its neighbors' new node equivalents to its own new node equivalent
        for oldNode in oldToNew.keys():
            for nb in oldNode.neighbors:
                oldToNew[oldNode].neighbors.append(oldToNew[nb])

        return oldToNew[node] # Return new version of node 1