'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
'''

def characterReplacement(s, k):
    l = 0
    res = 0
    hsh = {}
    length = 0
    for i in range(len(s)):
        length += 1
        if s[i] not in hsh:
            hsh[s[i]] = 1
        else:
            hsh[s[i]] += 1
        if(length - max(hsh.values()-k <= 0)):
            res += 1
        else:
            length -= 1
            hsh[s[l]] -= 1
            l += 1
    return res
