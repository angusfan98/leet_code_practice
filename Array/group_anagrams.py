import collections 

'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]
'''

def groupAnagrams(strs):
    hsh = collections.defaultdict(list)
    for s in strs:
        key_val = [0] * 26
        for i in s:
            key_val[ord(i) - ord("a")] += 1
        hsh[tuple(key_val)].append(s)
    return hsh.values()

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))

'''
Comments:

Determining if the strings are anagrams by checking the letter count of each word then utilizing this as a key in the hash table to group them together.

Time complexity: O(NM) where N is the length of strs and M is the maximum length of a string.
Space complexity: O(NM). The hash table is of size NM
'''
