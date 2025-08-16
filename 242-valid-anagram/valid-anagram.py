# Read characters from s, add to dict w value 1
# If already exists, increment value (=count)
# Read characters from t and check if in dict w/ value > 0
# If yes, decrement; if no, return false
# If all values in dict are zero, return true (else false)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        
        for c in s:
            if c in sdict:
                sdict[c] = sdict[c] + 1
            else:
                sdict[c] = 1

        for c in t:
            if c in sdict:
                sdict[c] = sdict[c] - 1
            else:
                return False
        
        for v in sdict.values():
            if v != 0:
                return False

        return True