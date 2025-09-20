class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # DP table with cells up to i=amount
        dp = [2**31] * (amount + 1)

        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                # If coin can get us backward without overshooting,
                # see how many steps it takes to reach index 0
                if c <= i:
                    # Calculate moves needed to reach index 0
                    # Update if less than previous calculations
                    moves = 1 + dp[i - c]
                    if moves < dp[i]:
                        dp[i] = 1 + dp[i - c]
        
        if dp[amount] == 2**31: # No solution
            return -1
        return(dp[amount])