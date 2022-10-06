'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''

def isValid(s):
    stack = []
    hsh = { ")":"(",
            "]":"[",
            "}":"{"}
    for i in range(len(s)):
        if s[i] in hsh:
            if stack and stack[-1] == hsh[s[i]]:
                stack.pop()
            else:
                return False
        else:
            stack.append(s[i])
    if stack:
        return False
    else:
        return True
