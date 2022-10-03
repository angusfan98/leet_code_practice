'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
'''

def longestConsecutive(nums):
    longest = 0
    set_num = set(nums)
    for i in range(len(nums)):
        if nums[i]-1 not in set_num:
            length = 0
            while nums[i] + length in set_num:
                length += 1
            longest = max(length, longest)
    return longest

nums = [100,4,200,1,3,2]
nums2 = [0,3,7,2,5,8,4,6,0,1]

def test_longestConsecutive():
    assert longestConsecutive(nums) == 4
    assert longestConsecutive(nums2) == 9
