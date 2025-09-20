# Iterate through magazine to see what we're workin with
# Add letters to a dictionary w\ value 1, incrementing said value if already present
# Iterate through letter to see what we need
# Subtract from dict value when letter used; remove if val hits 0
# If any letter is not present when needed, fail
# Otherwise success

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magLetters = dict() # Letters we can use

        # For each char, increment respective dict entry
        for char in magazine:
            if char in magLetters:
                magLetters[char] += 1
            else:
                magLetters[char] = 1

        # Now check whether each letter in the note is available
        for char in ransomNote:
            if char in magLetters:
                # Use up one instance of the char
                magLetters[char] -= 1
                
                # Remove fully expended characters
                # If encountered again, char will trigger the False exit condition
                if magLetters[char] == 0:
                    del magLetters[char]
            else:
                return False
        
        return True