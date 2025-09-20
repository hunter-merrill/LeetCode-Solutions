# To use the most numbers, you obviously wanna start with the smallest ones
# (to contribute the least to the sum each time)
# But eventually you'll get to a number that EITHER equals the remaining sum
# --> Hooray! Append it and we're done
# OR, more likely, it's *too big* and so you gotta rethink something.
# --> Since our algorithm guarantees that this too-big number is also the SMALLEST unused number,
# We gotta REPLACE a number w/ the new too-big number.
# Do some simple mind-algebra and you'll see that we gotta replace the number that
# equals the difference between the overflowed sum and the target sum (which will ofc be even & used).

class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        used = set() # Set of numbers we've included so far
        if (not finalSum) or (finalSum % 2 != 0): return used

        lastUsed = 0
        runningSum = 0
        while runningSum < finalSum:
            lastUsed += 2

            # Number doesn't overflow the sum
            if runningSum + lastUsed <= finalSum:
                runningSum += lastUsed
                used.add(lastUsed)
            
            # Number overflows sum
            # Note: due to nature of algorithm, overflow is ALWAYS magnitude 2
            else:
                # Add next number
                runningSum += lastUsed
                used.add(lastUsed)
                
                # Remove difference
                used.remove(runningSum - finalSum)
                
        return used