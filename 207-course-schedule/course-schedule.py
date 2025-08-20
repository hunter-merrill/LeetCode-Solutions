# This is a graph problem in disguise! Courses are nodes, prereqs are directed edges.
# Build adjacency list
# DFS
# If loop is found, return False

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    
        # Create adjacency list
        adjacent = {i: [] for i in range(numCourses)}

        # Add prereqs to respective course's adjacencies
        for p in prerequisites:
            adjacent[p[0]].append(p[1])

        # List of courses left to check
        courses = {i for i in range(numCourses)}
        visited = {i:0 for i in range(numCourses)}
        
        # DFS on all prereqs
        # If none, return list of visited nodes
        def dfs(course):
            # Never check redundant course
            if visited[course] == 1:
                return False # Cycle
            if visited[course] == 2:
                return True # Already checked
            
            visited[course] = 1
            for prereq in adjacent[course]:
                if not dfs(prereq):
                    return False
            visited[course] = 2
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True