'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
'''

def search(nums,target):
    r = 0
    l = len(nums)-1
    while r <= l:
        middle = (l+r)//2
        if nums[middle] == target:
            return middle
        elif target > nums[middle]:
            r = middle + 1
        else:
            l = middle - 1
    return -1

print(search([-1,0,3,5,9,12],9))