# Cheat solution: treat it like 3 cases
# Case two+ zeroes: return list of 0
# Case one zero: return list of 0 except index of 0 = product of the rest of the list
# Case no zeros: return the thing I put down there

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        zeroIdx = None
        lenNums = len(nums)

        numsProduct = 1
        for i in range(lenNums): 
            
            if nums[i] == 0:
                if zeroIdx == None: zeroIdx = i # Case one zero (or, the first zero when there are 2+)
                else: return [0] * lenNums # Case two+ zeroes
            else: numsProduct *= nums[i]
        
        # Case one zero
        if zeroIdx != None:
            return ([0] * zeroIdx) + [numsProduct] + ([0] * (lenNums - zeroIdx - 1)) # List of zeroes, except where zero was at

        # Case no zeroes
        return [int(numsProduct * num**-1) for num in nums]