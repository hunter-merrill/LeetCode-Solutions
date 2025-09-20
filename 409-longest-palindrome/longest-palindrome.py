from collections import defaultdict

# Pass through the string and count how many of each letter we got
# When count reaches 1, increase single count
# When count reaches 2, reset it to 0, increase pair count, decrease single count
# Number of letters in longest palindrome = 2 * number of pairs (+1 if there's a single)

class Solution:
    def longestPalindrome(self, s: str) -> int:
        pairs = 0
        singles = 0
        letterCounts = defaultdict(int)
        
        for letter in s:
            letterCounts[letter] = letterCounts[letter] + 1

            if letterCounts[letter] == 2:
                pairs += 1
                singles -= 1
                letterCounts[letter] = 0
            else:
                singles += 1
        
        return (2 * pairs) + min(1, singles)