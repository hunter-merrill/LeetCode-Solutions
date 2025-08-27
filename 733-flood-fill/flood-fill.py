# DFS

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        visited = set()
        starting_color = image[sr][sc]
        xBound = len(image)
        yBound = len(image[0])

        def dfs(pixel: tuple):
            # Fill pixel and mark seen
            image[pixel[0]][pixel[1]] = color
            visited.add(pixel)

            # Explore up/down/left/right
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                xNew = pixel[0] + x
                yNew = pixel[1] + y
                
                # Check against image bounds
                if not (-1 < xNew < xBound) or not (-1 < yNew < yBound):
                    continue

                # If number matches starting color, flood and continue fill
                if (xNew, yNew) not in visited and image[xNew][yNew] == starting_color:
                    dfs((xNew, yNew))

        dfs((sr, sc))
        return image