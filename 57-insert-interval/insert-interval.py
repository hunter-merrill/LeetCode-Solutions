# Binary search over first element of list
# Once insert position found, check interval end at i-1 to see if it overlaps
# If so, collapse leftward by larger end index
# Check interval start at i+1 to see if it overlaps
# If so, collapse leftward by larger end index UNTIL intervals[i+1][0] > intervals[i][1]
# [1,2] [3,5] [7,9]
# [0,10]

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if not intervals:
            return [newInterval]

        intervals.append(newInterval)
        intervals.sort()

        collapsedIntervals = [intervals[0]]
        prev = collapsedIntervals[0]
        for i in range(1, len(intervals)):
            
            curr = intervals[i]
            if curr[0] <= prev[1]: # Start is WITHIN previous interval
                prev[1] = max(curr[1], prev[1]) # Collapse and pick the bigger of the ends
            else:
                collapsedIntervals.append(curr)
                prev = curr

        return collapsedIntervals