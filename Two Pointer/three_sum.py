'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''

def threeSum(nums):
    res = []
    nums.sort()

    def twosumhelper(i,nums,res):
        r = i+1
        l = len(nums)-1
        while r < l:
            sum = nums[i] + nums[r] + nums[l]
            if sum == 0:
                res.append([nums[i],nums[r],nums[l]])
                r = r + 1
                l = l - 1
                while r < l and nums[r] == nums[r-1]:
                    r = r + 1
            elif sum > 0:
                l = l - 1
            else:
                r = r + 1

    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i == 0 or nums[i-1] != nums[i]:
            twosumhelper(i,nums,res)
    return res
    
nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))