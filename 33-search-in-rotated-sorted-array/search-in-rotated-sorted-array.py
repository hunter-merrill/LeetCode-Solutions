# O(log n) is easy on a regular sorted array
# If we can find the barrier of rotation (nums[i] > nums[i+1]) in
#   O(log n) time, then the complexity of the overall solution will
#   remain the same as the subsequent binary search
#
# We want to keep the same time complexity as binary search?? Then let's just
#   do binary search twice
# First searching for the aforementioned barrier instead of a specific element

class Solution(object):
    def search(self, nums, target):
        
        n = len(nums)

        def findRotation():

            l = 0
            r = n - 1
            mid = -1

            # Edge case: no rotation or single-element list
            if nums[0] <= nums[-1]:
                return 0
            
            # Search for nums[i] > nums[i+1]
            while nums[l] > nums[r]:
                
                mid = (l + r + 1) // 2 # Index of centermost element
                
                if nums[mid] < nums[l]:
                    r = mid - 1 # Case: rotation barrier is to the left of midpoint
                else:
                    l = mid # Case: rotation barrier is to the right of midpoint
            
            return n - mid

        def rotatedBinSearch(rot):

            l = 0
            r = n - 1
            mid = midRot = -1
            
            while l < r:
                
                mid = (l + r + 1) // 2
                midRot = (mid - rot) % n
                
                if nums[midRot] > target:
                    r = mid - 1
                else:
                    l = mid

            lRot = (l - rot) % n
            if nums[lRot] == target:
                return lRot
            else:
                return -1
        
        rot = findRotation()
        return rotatedBinSearch(rot)

