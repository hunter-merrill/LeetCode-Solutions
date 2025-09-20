from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        halfway = len(nums) / 2
        appearances = defaultdict(int)
        
        for num in nums:
            appearances[num] = appearances[num] + 1

            if appearances[num] >= halfway:
                return num