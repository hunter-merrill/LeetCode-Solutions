# Binary search intervals for the correct place to insert newInterval's head
# Label this l
# (Correct place is where left interval ends before & right interval starts after,
# or where either bound matches newInterval's left bound)
# Search the space to the right of that point for the correct place for newInterval's right bound
# If the right bound of the left neighboring interval equals or exceeds newIntervals' own, replace it with newInterval's right bound
# Vice versa w the left bound at the right neighbor
# If overlap w two intervals at once, update left one's right bound to equal right one's left bound - 1

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if len(intervals) == 0:
            return [newInterval]

        # Left and right feelers
        # Start in middle
        # Return ind of target
        def binaryIntervalSearch(arr, targetVal):
            l, r = 0, len(arr) - 1
            mid = int((l + r) / 2)

            while l < r:
                # Get element at center of unchecked range
                # Select bound specified by parameters
                curr = arr[mid]
                
                # If left bound too big, contract range from the right
                if curr[0] > targetVal:
                    r = mid - 1
                # If left bound too small, check right bound
                elif curr[0] < targetVal:
                    # If right bound too small, contract range from the left
                    if curr[1] < targetVal:
                        l = mid + 1
                    # If not, then target is contained by this interval
                    else: r = l = mid
                # Left bound == target
                else: r = l = mid
                
                mid = int((l + r) / 2)
            
            return mid

        leftInterval = binaryIntervalSearch(intervals, newInterval[0])
        rightInterval = binaryIntervalSearch(intervals, newInterval[1])
        print(leftInterval)
        print(rightInterval)

        # For the interval at each returned index, check whether newInterval's 
        # respective bound is to the left, contained, or to the right

        collapsed = []
        if newInterval[0] < intervals[leftInterval][0]:
            collapsed.append([newInterval[0], -1])
        elif newInterval[0] > intervals[leftInterval][1]:
            collapsed.append(intervals[leftInterval])
            collapsed.append([newInterval[0], -1])
        else:
            collapsed.append(intervals[leftInterval])
        print(collapsed)
        if newInterval[1] < intervals[rightInterval][0]:
            collapsed[len(collapsed) - 1][1] = newInterval[1]
            collapsed.append(intervals[rightInterval])
        elif newInterval[1] > intervals[rightInterval][1]:
            collapsed[len(collapsed) - 1][1] = newInterval[1]
        else:
            collapsed[len(collapsed) - 1][1] = intervals[rightInterval][1]

        print(collapsed)
        intervals = intervals[:leftInterval] + collapsed + intervals[(rightInterval + 1):]
        print(intervals)
        return intervals