'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]


Example 2:

Input: nums = [1], k = 1
Output: [1]
'''

def topKFrequent(nums,k):
    res = []
    length = len(nums)
    hsh = {}
    for i in range(length):
        if nums[i] not in hsh:
            hsh[nums[i]] = 1
        else:
            hsh[nums[i]] += 1
    arr = [[] for i in range(length+1)]
    for key in hsh:
        arr[hsh[key]].append(key)
    print(arr)
    for i in reversed(range(len(arr))):
        for j in arr[i]:
            res.append(j)
            if len(res) == k:
                return(res)

def test_topKFrequent():
    assert topKFrequent([1,1,1,2,2,3],2) == [1,2]
    assert topKFrequent([1],1) == [1]

'''
Comments:

Utilizing a hash table to determine the frequency of each element in the array. Then we create an array of lists to store the value from the hash table.
We can then loop backwards to see the k most frequent elements.

Time complexity: O(N). Utilizing the array we created that is at most the length of nums allows us to have loops that are at most O(N) time complexity.
Space complexity: O(N). Creating a hash table and an extra array of size N.
'''