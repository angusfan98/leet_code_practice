'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''

def maxProfit(arr):
    min_price = float('inf')
    res = 0
    for i in range(len(arr)):
        if arr[i] < min_price:
            min_price = arr[i]
        if arr[i] - min_price > res:
            res = arr[i] - min_price
    return res

def test_maxProfit():
    assert maxProfit([7,1,5,3,6,4]) == 5
    assert maxProfit([7,6,4,3,1]) == 0

'''
Comments:

Utilizing a hash table using one pass-through of the array

Time complexity: O(n): One for-loop is needed to determine the lowest price and we just need to see the highest point after that
Space complexity: O(1)
'''