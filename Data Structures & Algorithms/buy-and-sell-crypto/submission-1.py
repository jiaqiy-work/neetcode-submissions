class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minPrice = prices[0]

        for sell in prices:
            maxP = max(maxP, sell-minPrice)
            minPrice = min(minPrice, sell)
        return maxP