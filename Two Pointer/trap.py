'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
'''

def trap(height):
    sum = 0
    max_left = [0]*len(height)
    max_right = [0]*len(height)
    cur_max_left = -2**31
    cur_max_right = -2**31
    for i in range(1,len(height)):
        cur_max_left = max(cur_max_left, height[i-1])
        max_left[i] = cur_max_left
    for i in range(1,len(height)):
        cur_max_right = max(cur_max_right, height[(len(height)-i)])
        max_right[(len(max_right)-i-1)] = cur_max_right
    for i in range(len(height)):
        if min(max_left[i],max_right[i]) - height[i] > 0:
            sum += min(max_left[i],max_right[i]) - height[i]
    return sum


height = [0,1,0,2,1,0,1,3,2,1,2,1]
height_2 = [4,2,0,3,2,5]

def test_trap():
    assert trap(height) == 6
    assert trap(height_2) == 9