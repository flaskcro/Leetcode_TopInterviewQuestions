"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock.
You can only hold at most one share of the stock at any time.
However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > buy:
                profit += (prices[i] - buy)
            buy = prices[i]

        return profit


if __name__ == "__main__":
    solution = Solution()
    prices = [7,1,5,3,6,4]
    assert solution.maxProfit(prices) == 7

    prices = [1, 2, 3, 4, 5]
    assert solution.maxProfit(prices) == 4

    prices = [7,6,4,3,1]
    assert solution.maxProfit(prices) == 0
