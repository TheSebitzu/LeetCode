class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize price with a big value (inf)
        min_price = float('inf')
        max_profit = 0
        # Iterate through the list
        for price in prices:
            
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit