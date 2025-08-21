from collections import deque

# Similar soln to #200
# Just use BFS (or DFS) to make a wave through Os
# If that wave touches an edge, do nothing
# If not (i.e. it's contained), convert it all to X
# The trick to efficiency is to crawl the border at first to determine which regions are not containable

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()

        def bfs(row, col):
            q = deque([(row, col)])
            contained = True

            # Start a wave over the area of this region
            while q:
                currRow, currCol = q.popleft()
                
                for shift in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    newRow, newCol = currRow + shift[0], currCol + shift[1]
                
                    # Check if border
                    if not (0 <= newRow < len(board)) or not (0 <= newCol < len(board[0])):
                        contained = False

                    # Continue wave
                    elif board[newRow][newCol] == 'O' and (newRow, newCol) not in visited:
                        visited.add((currRow, currCol))
                        q.append((newRow, newCol))
                        board[newRow][newCol] = 'U' # Mark uncontained

        for row in range(len(board)):
            # Upper & lower perimeter
            if row == 0 or row == len(board) - 1:
                cols = range(len(board[0]))
            # Left & right perimeter
            else:
                cols = [0, len(board[0]) - 1]

            for col in cols:
                if board[row][col] == 'O' and (row, col) not in visited:
                    board[row][col] = 'U' # Mark uncontained
                    bfs(row, col)
        
        # Convert remaining (contained) Os to Xs, and return Us to Os
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'U':
                    board[row][col] = 'O'
                elif board[row][col] == 'O':
                    board[row][col] = 'X'