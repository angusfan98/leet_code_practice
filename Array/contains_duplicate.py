'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''

def containsDuplicate(arr):
    hsh_tbl = {}
    for i in range(len(arr)):
        if arr[i] not in hsh_tbl:
            hsh_tbl[arr[i]] = 1
        else:
            hsh_tbl[arr[i]] = hsh_tbl[arr[i]] + 1
    for key in hsh_tbl:
        if hsh_tbl[key] > 1:
            return True
    return False

def test_containsDuplicate():
    assert containsDuplicate([1,2,3,1]) == True
    assert containsDuplicate([1,2,3,4]) == False
    assert containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True

'''
Comments:
'''