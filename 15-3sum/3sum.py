# Double-layer DP
# 2Sum n times

class Solution:
    def threeSum(self, nums):
        
        if len(nums) < 3:
            return []
        
        n = len(nums)
        nums.sort()
        triplets = []

        for i, num in enumerate(nums[:-2]):
            
            # Case: duplicate 
            if i >= 1 and num == nums[i-1]:
                continue
            
            l, r = i+1, n-1
            target = -num

            while l < r:
                if nums[l] + nums[r] == target:
                    triplets.append([num, nums[l], nums[r]])

                    # Avoid duplicates
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1

                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
                
        return triplets