'''
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.
'''

def maxSlidingWindow(nums,k):
    if len(nums) == 1 and k == 1:
        return [nums[0]]
    else:
        r = 0 
        l = k
        res = []
        while l < len(nums)+1:
            res.append(max(nums[r:l]))
            r = r + 1
            l = l + 1
        return res


print(maxSlidingWindow([1,2],1))