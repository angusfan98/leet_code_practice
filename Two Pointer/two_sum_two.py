'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
'''

def twoSum(nums,target):
    l = 0
    r = len(nums)-1
    while l < r:
        if nums[l] + nums[r] == target:
            return([l+1,r+1])
        elif nums[l] + nums[r] > target:
            r = r - 1
        else:
            l = l +  1



numbers = [2,7,11,15]
numbers_2 = [2,3,4]
numbers_3 = [-1,0]
target = 9
target_2 = 6
target_3 = -1
def test_twoSum():
    assert twoSum(numbers,target) == [1,2]
    assert twoSum(numbers_2,target_2) == [1,3]
    assert twoSum(numbers_3,target_3) == [1,2]