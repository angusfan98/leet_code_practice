'''
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.
'''

def minWindow(s,t):
    hsh_t = {}
    for c in t:
        hsh_t[c] = 1 + hsh_t.get(c,0)

    cur = {}
    have = 0
    need = len(hsh_t)
    res = []
    resLen = float("infinity")
    l = 0
    for r in range(len(s)):
        cur[s[r]] = 1 + cur.get(s[r],0)

        if s[r] in hsh_t and cur[s[r]] == hsh_t[c]:
            have += 1
        while have == need:
            if (r - l + 1) < resLen:
                res = [l,r]
                resLen = (r-1+1)
            cur[s[l]] -= 1
            if s[l] in hsh_t and cur[s[l]] < hsh_t[s[l]]:
                have -= 1
            l += 1
    l,r = res
    return s[l:r+1] if resLen != float("infinity") else ""


print(minWindow("ADOBECODEBANC","ABC"))