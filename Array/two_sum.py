import pytest

'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''

def twoSum(arr,target):
    hsh_tbl = {}
    for i in range(len(arr)):
        comp = target - arr[i]
        if arr[i] not in hsh_tbl:
            hsh_tbl[comp] = i
        else:
            return[hsh_tbl[arr[i]],i]
    

def test_twoSum():
    assert twoSum([3,2,4],6) == [1,2]
    assert twoSum([3,3],6) == [0,1]
    assert twoSum([2,7,11,15],9) == [0,1]

'''
Comments:

Utilizing a hash table using one pass-through of the array

Time complexity: O(n). The array contains n elements and the look up of a hash table cost O(1) time
Space complexity: O(n). Extra space is at most n elements since that is the number of items stored in the hash table.
'''