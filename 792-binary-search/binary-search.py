class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        mid = (l + r) // 2

        while l <= r:
            curr = nums[mid]
            
            if curr > target:
                r = mid - 1
            elif curr < target:
                l = mid + 1
            elif curr == target:
                return mid

            mid = (l + r) // 2
        
        return -1