class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or prices is []:
            return 0

        min = prices[0]
        profit = 0

        for i in range(len(prices)):
           if prices[i] < min:
               min = prices[i]

           profit = max(profit, (prices[i] - min))

        return profit