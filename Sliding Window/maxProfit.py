'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

def maxProfit(prices):
    cur_min = 2**31-1
    res = 0
    for i in range(len(prices)):
        cur_min = min(cur_min, prices[i])
        res = max(res, (prices[i]-cur_min))
    return res

prices = [7,1,5,3,6,4]
prices_2 = [7,6,4,3,1]

def test_maxProfit():
    assert maxProfit(prices) == 5
    assert maxProfit(prices_2) == 0