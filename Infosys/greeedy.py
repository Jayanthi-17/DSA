'''
Given an array prices[] of non-negative integers, representing the prices of the stocks on different days. The task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell. If it is not possible to make a profit then return 0.

Note: Stock must be bought before being sold.
'''

class Solution:
    def maxProfit(self, prices):
        n=len(prices)
        min_price=float("inf")
        max_profit=0
        for i in range(n):
            price =prices[i]
            if price< min_price:
                min_price=price
            profit=price-min_price
            if profit>max_profit:
                max_profit=profit
        return max_profit