# Hash table/dict approach: bypasses need to search list for complement

class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}
        length = len(nums)
        
        for i in range(length):
            curr = nums[i]
            complement = target - curr
            
            if complement in hashmap:
                return [i, hashmap[complement]]
            
            hashmap[curr] = i