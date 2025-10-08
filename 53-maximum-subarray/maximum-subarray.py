# Naive: calculate the sum of all possible subarrays
# O(n^2)
# 
# DP problem, remember the sums bc they contribute to each other --> overlapping subproblems
# idea: lookup table using start & end idx
# 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        local_max = -inf
        global_max = -inf
        
        for num in nums:
            local_max = max(num, local_max + num)
            global_max = max(global_max, local_max)
        
        return global_max