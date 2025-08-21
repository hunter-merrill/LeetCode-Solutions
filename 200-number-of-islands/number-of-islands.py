# 2D array of tile coordinates & whether they're part of an island or not
# Check neighbors to see if part of existing island
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numAdded, numMerged = 0, 0 # Islands added and removed during the process; used to calculate numIslands
        islands = {} # Keeps track of islands & their tiles

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                upper, left, lower, right = '0', '0', '0', '0'
                currTile = grid[row][col]

                # If water, obv not island
                if currTile == '0':
                    continue
                
                # Check upper tile
                if row > 0:
                    upper = grid[row - 1][col]
                    if upper is not '0':
                        grid[row][col] = upper
                        islands[upper].add((row, col))
                
                # Check left tile
                if col > 0:
                    left = grid[row][col - 1]
                    if left is not '0':
                        grid[row][col] = left
                        islands[left].add((row, col))

                # Check if tile connects two previous islands
                if upper is not '0' and left is not '0' and upper != left:
                    
                    # Oldest island remains, younger one gets annexed
                    toMerge = 0
                    mergedInto = 0

                    # Determine which island was there first
                    if int(upper) < int(left):
                        mergedInto = upper
                        toMerge = left
                    elif int(upper) > int(left):
                        mergedInto = left
                        toMerge = upper
                    
                    # Convert false island's tiles into target island tiles
                    for tile in islands[toMerge]:
                        grid[tile[0]][tile[1]] = mergedInto
                        islands[mergedInto].add((tile[0], tile[1]))
                    del islands[toMerge]
                    numMerged += 1

                # New island
                if upper is '0' and left is '0':
                    numAdded += 1

                    # Keeps track of which tiles are in which island
                    islands[numAdded] = {(row, col)}
                    grid[row][col] = numAdded

        return numAdded - numMerged

                


                