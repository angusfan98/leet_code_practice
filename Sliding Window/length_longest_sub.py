'''
Given a string s, find the length of the longest substring without repeating characters.
'''

def lengthOfLongestSubstring(s):
    cur = []
    cur_length = 0
    max_length = 0
    for i in range(len(s)):
        while s[i] in cur:
            cur.pop(0)
            cur_length -= 1
        cur.append(s[i])
        cur_length += 1
        max_length = max(cur_length,max_length)
    return max_length




s = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"

def test_lengthoflongest():
    assert lengthOfLongestSubstring(s) == 3
    assert lengthOfLongestSubstring(s2) == 1
    assert lengthOfLongestSubstring(s3) == 3