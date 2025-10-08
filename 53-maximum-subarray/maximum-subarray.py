# Kadane
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        local_max = -inf
        global_max = -inf
        
        for num in nums:
            local_max = max(num, local_max + num)
            global_max = max(global_max, local_max)
        
        return global_max