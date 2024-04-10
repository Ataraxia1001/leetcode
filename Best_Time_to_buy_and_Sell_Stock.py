class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        min_buy = prices[0]
        for i in range(len(prices)):
            if prices[i] > min_buy:
                continue

            for k in range(i+1, len(prices)):
                if prices[k] == 0 or prices[k] < prices[i]:
                    continue
                profit = prices[k] - prices[i]
             
                if profit >= max_profit:
                    max_profit = profit
                    min_buy = prices[i]


        return max_profit
    
# 208 / 212 testcases passed