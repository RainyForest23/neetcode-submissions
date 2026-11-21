# start : 23:37
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = [[0 for _ in range(len(prices))] for _ in range(len(prices))]
        # 2-dimension array
        # list comprihansion 알아두자..
        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         profit = prices[j] - prices[i]
        #         if profit >= max_profit:
        #             max_profit = profit
        # return max_profit

                
        # O(n) soltion

        min_price = prices[0]   # 지금까지 본 최저가
        max_profit = 0          # 지금까지 찾은 최대 수익

        for price in prices:
            profit = price - min_price        # 1. 오늘 팔면 수익
            if profit > max_profit:           # 2. 최대 수익 갱신
                max_profit = profit
            if price < min_price:             # 3. 최저가 갱신
                min_price = price

        return max_profit

            