# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # 1. Node splits p and q (<= one & >= the other): return Node
        # 2. Both to left: continue search on left child
        # 3. Both to right: continue search on right child

        lowest = root
        pVal, qVal = p.val, q.val
        while lowest:
            lowVal = lowest.val
            
            # Case 1.
            if lowVal <= pVal and lowVal >= qVal or lowVal >= pVal and lowVal <= qVal:
                return lowest
            
            # Case 2.
            if lowVal > pVal and lowVal > qVal:
                lowest = lowest.left
            # Case 3.
            elif lowVal < pVal and lowVal < qVal:
                lowest = lowest.right
            else:
                print("Huh? Case 4.")
        print("Huh? No return")