from collections import deque

# Essentially BFS until none fresh
#   --> catch impossibility somehow to avoid infinite loop
#
# Naive solution: per minute, scan entire array for rotten oranges, updating neighbors
# O(m*n*t)
# 
# Thought: Never need to check a rotten orange from previous time -- its neighbors are already affected
# First pass: Find rotten, store coords
# Then: Update neighbors of rotten, store coords
# If new rotten created, update minute
# Repeat with the rotten oranges we just created
#
# End condition: No new rotten oranges created
#   --> Works for both possible & impossible matrices
#       Final pass to check if any non-rotten left over?

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        t = 0
        m = len(grid)
        n = len(grid[0])
        
        fresh = set()
        rotten = deque()

        # First pass: Add fresh oranges to memo and rotten oranges to queue
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh.add((r, c))
                elif grid[r][c] == 2:
                    rotten.append((r, c))
        
        numRotten = len(rotten) # Used to track time intervals
        while rotten:

            orange = rotten.popleft() # Get first-added orange
            numRotten -= 1 # Decrement number of oranges from previous interval left to visit

            # Visit neighbors
            for x, y in [(1,0), (-1,0), (0,1), (0,-1)]:
                xNew = orange[0] + x
                yNew = orange[1] + y

                # Out-of-bounds checking
                if not(0 <= xNew < m) or not(0 <= yNew < n):
                    continue

                # Turn fresh oranges rotten, add to queue, remove from memo
                if grid[xNew][yNew] == 1:
                    grid[xNew][yNew] = 2
                    rotten.append((xNew, yNew))
                    fresh.remove((xNew, yNew))
            
            # At end of time interval, increment time if new oranges were created
            if numRotten == 0:
                if rotten:
                    t += 1
                    numRotten = len(rotten) # Number of oranges in next time interval

        # If fresh oranges remaining, rotting failed
        if fresh:
            return -1
        
        # All rotted, report time elapsed
        return t