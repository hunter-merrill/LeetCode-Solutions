class Solution(object):
    def sortColors(self, nums, max_color=2):
        counts = [0] * (max_color + 1) # Number of times each color occurs in nums
        firsts = [0] * (max_color + 1) # Starting pos of each color in sorted array

        # For each element, increment count & move back starting pos of each following color
        for i in range(len(nums)):
            n = nums[i]
            counts[n] += 1

            color = n
            while color < max_color:
                nextColor = color + 1
                
                if i >= firsts[nextColor]:
                    replace = nums[firsts[nextColor]]
                    nums[i] = replace
                    nums[firsts[nextColor]] = color

                if counts[nextColor] == 0:
                    break
                    
                color += 1
            
            for color in range(1, max_color + 1):
                firsts[color] += int(n < color)