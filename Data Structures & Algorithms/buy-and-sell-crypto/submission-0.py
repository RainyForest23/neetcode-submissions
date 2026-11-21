# start : 23:37
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = [[0 for _ in range(len(prices))] for _ in range(len(prices))]
        # 2-dimension array
        # list comprihansion 알아두자..
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                if profit >= max_profit:
                    max_profit = profit
        return max_profit

                
                # profit[i][j] = i - j

        