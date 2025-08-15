# Because of the rule that you must buy before you sell,
# there is no need to check previous days' profit margins
# on new minimum prices. Thus, a single-pass solution is simple.
#
# Initialize lowest price to the first day's price, max profit to 0
# Check each day: if lower, update lowest; if profit higher, update max profit
# Return
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        maxProfit = 0

        for p in prices:
            # If new lowest price, update minimum & continue
            if p < low:
                low = p
                continue
            
            # If new greatest profit, update maximum
            profit = p - low
            if profit > maxProfit:
                maxProfit = profit
        
        return maxProfit