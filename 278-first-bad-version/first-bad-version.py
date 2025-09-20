# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        left, right = 1, n
        currVersion = (left + right) // 2
        while left < right:
            
            if(isBadVersion(currVersion)):
                right = currVersion
            else:
                left = currVersion + 1

            currVersion = (right + left) // 2

        return currVersion