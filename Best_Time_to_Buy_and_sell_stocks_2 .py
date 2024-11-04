class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        buy = prices[0]
        for i in range(0,len(prices)):
            if buy < prices[i]:
                max += prices[i] - buy
            buy = prices[i]
        return max
        