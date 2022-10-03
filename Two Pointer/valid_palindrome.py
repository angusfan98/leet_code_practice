'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''

def isPalindrome(s):
    new_s = ''.join(filter(str.isalnum, s))
    new_s = new_s.lower()
    l = 0
    r = len(new_s)-1
    for i in range(len(new_s)):
        print(new_s[r])
        if new_s[r] == new_s[l]:
            r = r-1
            l = l+1
        else:
            return False
    return True

s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"

print(isPalindrome(s1))


def test_isPalindrome():
    assert isPalindrome(s1) == True
    assert isPalindrome(s2) == False