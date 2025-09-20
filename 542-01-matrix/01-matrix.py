class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        # Null array
        if not mat:
            return mat

        # Matrix dimensions
        nrow = len(mat)
        ncol = len(mat[0])
        
        def checkNeighbor(r, c, direction):
            # No need to check neighbors if 0
            if mat[r][c] == 0:
                return 0
            
            # Find least of neighbors
            minVal = float('inf')
            for x, y in [(direction, 0), (0, direction)]:    
                
                # Neighbor's coords
                rNew = r + x
                cNew = c + y  
                
                # Skip if OOB
                if not (0 <= rNew < nrow) or not (0 <= cNew < ncol):
                    continue
                
                # Check neighbor's dist from zero
                neighborVal = mat[rNew][cNew]
                if neighborVal < minVal:
                    minVal = neighborVal

                # Can't get loewr than zero! unless your distance is negative but let's not go there
                if minVal == 0:
                    break

            # Update tile value
            # If second pass, compare to first pass value as well
            mat[r][c] = min(mat[r][c], minVal + 1) if direction == 1 else minVal + 1

        # Breadth-first search the matrix
        for r in range(nrow):
            for c in range(ncol):
                checkNeighbor(r, c, -1)
        for r in reversed(range(nrow)):
            for c in reversed(range(ncol)):
                checkNeighbor(r, c, 1)
        
        return mat