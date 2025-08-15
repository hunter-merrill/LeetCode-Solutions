from collections import deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Hash map for alphanumerics that converts caps into lowercase
        # It would be nicer to do this programatically but I don't wanna lose precious milliseconds :,)
        alphanumeric = {
            '1': '1', '2': '2', '3': '3', '4': '4', '5': '5',
            '6': '6', '7': '7', '8': '8', '9': '9', '0': '0',
            'q': 'q', 'w': 'w', 'e': 'e', 'r': 'r', 't': 't',
            'y': 'y', 'u': 'u', 'i': 'i', 'o': 'o', 'p': 'p',
            'a': 'a', 's': 's', 'd': 'd', 'f': 'f', 'g': 'g',
            'h': 'h', 'j': 'j', 'k': 'k', 'l': 'l',
            'z': 'z', 'x': 'x', 'c': 'c', 'v': 'v', 'b': 'b',
            'n': 'n', 'm': 'm',

            'Q': 'q', 'W': 'w', 'E': 'e', 'R': 'r', 'T': 't',
            'Y': 'y', 'U': 'u', 'I': 'i', 'O': 'o', 'P': 'p',
            'A': 'a', 'S': 's', 'D': 'd', 'F': 'f', 'G': 'g',
            'H': 'h', 'J': 'j', 'K': 'k', 'L': 'l',
            'Z': 'z', 'X': 'x', 'C': 'c', 'V': 'v', 'B': 'b',
            'N': 'n', 'M': 'm'
        }
        dq = deque()
        
        # Pass 1: remove irrelevant characters
        reduced = []
        for c in s:
            if c in alphanumeric:
                reduced.append(alphanumeric[c])
        
        # Pass 2a: Queue the first half of the string
        length = len(reduced)
        for i in range(int(length/2)):
            dq.append(reduced[i])

        # Pass 2b: Compare second half to first (ignoring pivot if length is odd)
        for i in range(int((length+1)/2), length):
            if dq.pop() != reduced[i]:
                return False

        return True