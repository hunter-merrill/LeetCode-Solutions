from collections import deque

class Solution(object):
    def isValid(self, s):
        d = deque()
        d.append('start')
        
        # Dictionaries to check whether brackets match
        openPar = {
            '(': ')', 
            '[': ']', 
            '{': '}'
        }
        closedPar = {
            ')': '(', 
            ']': '[', 
            '}': '{'
        }
        
        # Iterate through characters in s
        for c in s:
            # Append (, [, { to deque
            if c in openPar:
                d.append(c)
            
            # Check ), ], } for matching open
            elif c in closedPar:
                if d.pop() != closedPar[c]:
                    return False
        
        # Check that all open brackets are closed
        return d.pop() == 'start'