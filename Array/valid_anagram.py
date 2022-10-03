'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true


Example 2:

Input: s = "rat", t = "car"
Output: false
'''

def valid_anagram(s,t):
    hash_one = {}
    hash_two = {}
    for i in range(len(s)):
        if s[i] not in hash_one:
            hash_one[s[i]] = 1
        else:
            hash_one[s[i]] += 1
    for i in range(len(t)):
        if t[i] not in hash_two:
            hash_two[t[i]] = 1
        else:
            hash_two[t[i]] += 1
    if hash_one == hash_two:
        return True
    else:
        return False

def test_valid_anagram():
    assert valid_anagram("anagram","nagaram") == True
    assert valid_anagram("rat","car") == False

'''
Comments:

Comparing two hash tables created from the two different strings to see if they are the same

Can optimize by checking the length first then utilizing one loop for creating two hash tables.

Time complexity: O(N). Accesing a hash table is O(n), two seperate for loops which are also O(n)
Space complexity: O(1). Table size is constant no matter how large n is.
'''
