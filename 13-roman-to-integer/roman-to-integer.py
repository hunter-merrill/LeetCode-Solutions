class Solution:
    def romanToInt(self, s: str) -> int:
        
        numeralValues = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        total = 0
        prev = 1001
        for i in range(len(s)):
            
            curr = numeralValues[s[i]]
            total += curr

            if curr > prev:
                total -= 2*prev

            prev = curr
        
        return total