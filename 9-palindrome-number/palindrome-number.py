from collections import deque

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        # 0 is obv a palindrome but it messes w my later logic so it gets special treatment
        if x == 0:
            return True

        # int can never start with 0 --> palindrome can't end with 0
        # int can never end with '-' --> palindrome can't start with - (i.e. no negatives)
        if (x % 10 == 0) or (x < 0):
            return False

        num = x
        dq = deque()
        
        # Add each digit to dq, starting from ones place
        while num > 0:                      # Iteration 1           # Iteration 2           # Iteration 3
            shiftLeft = num // 10           # 123 --> 12            # 12 --> 1              # 1 --> 0
            digit = num - (shiftLeft * 10)  # 123 - (12 * 10) = 3   # 12 - (1 * 10) = 2     # 1 - (0 * 10) = 1
            dq.append(digit)                # [3]                   # [3, 2]                # [3, 2, 1]
            num = shiftLeft                 # 12                    # 1                     # 0 --> break
        
        while len(dq) > 1:
            l, r = dq.popleft(), dq.pop()

            if l != r:
                return False

        return True