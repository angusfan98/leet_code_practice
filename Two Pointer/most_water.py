'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
'''

def maxArea(height):
    r = 0 
    l = len(height)-1
    max_area = 0 
    while r < l:
        area = min(height[r],height[l]) * (l-r)
        max_area = max(area,max_area)
        if (height[r] > height[l]):
            l = l - 1
        else:
            r = r + 1
    return max_area

height = [1,8,6,2,5,4,8,3,7]
height_2 = [1,1]

def test_maxArea():
    assert maxArea(height) == 49
    assert maxArea(height_2) == 1
