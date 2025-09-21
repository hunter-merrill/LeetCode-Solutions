#   123434564
#  "abcdbefgb"
#    123456789
#   123456789
#  1234567
# "abcdefaghib"
#
#  0       3
#  123456786
# "fh)(H$#T)$&GHfh89"
#  
#  0   1 2 3
#  1234455667
# "abcDaEbFcG"

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charIdx = {}
        startIdx = 0 # First char of the substring
        runningLen = maxLen = 0
        
        for i in range(len(s)):
            
            char = s[i]

            if char in charIdx:
                
                # Char seen before, but it was removed from the curr substr: Update charIdx
                if charIdx[char] < startIdx:
                    charIdx[char] = i

                # Duplicate char
                else:
                    substrIdx = (charIdx[char] - startIdx) # Index of first instance of char in current substr
                    newStartIdx = startIdx + substrIdx + 1 # Reset starting pos to one after first instance of repeated char
                    
                    maxLen = max(maxLen, runningLen)
                    runningLen -= (newStartIdx - startIdx) # Subtract characters no longer in substr from running total
                    startIdx = newStartIdx

            charIdx[char] = i # Update index of last-seen instance of char
            runningLen += 1

        return max(maxLen, runningLen)