# One pass
# Maintain a string of the longest prefix so far
# Go thru next word, stop when char not equal to next char in common prefix
# Break at end of word list OR when prefix = ""
# f l o w e r -
# f l o w -
# f l -
# end of input --> break

class Solution(object):
    def longestCommonPrefix(self, strs):

        pref = strs[0]
        
        for s in strs:
            if s == pref:
                continue
            
            running = []
            for i in range(len(s)):
                if i >= len(pref):
                    break
                if s[i] != pref[i]:
                    break
                running.append(s[i])
            
            pref = "".join(running)
        
        return pref