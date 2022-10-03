'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]


Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''


def productExceptSelf(nums):
    len_arr = len(nums)
    left_arr = [0]*len_arr
    right_arr = [0]*len_arr
    left_arr[0] = 1
    right_arr[len_arr-1] = 1
    for i in range(len_arr-1):
        left_arr[i+1] = left_arr[i]*nums[i]
    for i in range(len_arr-1):
        right_arr[len_arr-2-i] = right_arr[len_arr-1-i]*nums[len_arr-1-i]
    for i in range(len_arr):
        nums[i] = left_arr[i]*right_arr[i]
    return(nums)

def test_productExceptSelf():
    assert productExceptSelf([1,2,3,4]) == [24,12,8,6]
    assert productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]

'''
Comments:

Utilizing left and right arrays to combine for the result array.

Time complexity: O(N). N is the number of elements of the input array. One loop each for left array/right array/results array
Space complexity: O(N). Creating two extra arrays (left/right)
'''
