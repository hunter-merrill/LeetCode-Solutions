# Graph
# DFS on valid first chars
# Store info about neighbors of visited tiles to save repeat visits

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        wordFound = False
        visited = {}
        nrow = len(board)
        ncol = len(board[0])

        def dfs(node, nextCharIdx, currPath):
            nonlocal wordFound

            currPath.add(node) # Append node to current path of visited nodes

            # Word was found in different recursive branch
            if wordFound:
                return
            
            # Final letter of word was reached
            if nextCharIdx >= len(word):
                wordFound = True
                return
            
            if node not in visited:
                visited[node] = {} # Dict linking characters to neighbor tiles containing them
                # Visit neighbors
                # If char not in neighbors, make new list containing curr neighbor
                # If char alr in neighbors, append to list
                for x, y in [(-1,0), (1,0), (0,-1), (0,1)]:

                    # Coords of neighbor
                    xNew = node[0] + x
                    yNew = node[1] + y
                    
                    # Check if Out of Bounds
                    if not (0 <= xNew and xNew < nrow) or not (0 <= yNew and yNew < ncol):
                        continue

                    # Check if first instance of character
                    neighborChar = board[xNew][yNew]
                    if neighborChar not in visited[node]:
                        visited[node][neighborChar] = []
                    
                    # Append neighbor to list of neighbors w/ given char
                    visited[node][neighborChar].append((xNew, yNew))
            
            # If valid next character is adjacent, visit all nodes with that char
            #   and search for next char in string
            neighbors = visited[node] # List of CHARACTERS next to node
            nextChar = word[nextCharIdx]

            if nextChar in neighbors:
                for nextNode in neighbors[nextChar]:
                    # Check if already used
                    if nextNode in currPath:
                        continue 
                    dfs(nextNode, nextCharIdx + 1, currPath.copy())
        
        # Search for tiles w/ first char of word
        for row in range(nrow):
            for col in range(ncol):
                if board[row][col] == word[0]:
                    dfs((row, col), 1, set())

        return wordFound