'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''

def generateParenthesis(n):
    stack = []
    res = []
    def helper(openN, closedN):
        if openN == closedN == n:
            res.append("".join(stack))
            return

        if openN < n:
            stack.append("(")
            helper(openN + 1, closedN)
            stack.pop()
        if closedN < openN:
            stack.append(")")
            helper(openN, closedN + 1)
            stack.pop()

    helper(0, 0)
    return res

n = 3
n2 = 1

def test_gen():
    assert generateParenthesis(n) == ["((()))","(()())","(())()","()(())","()()()"]
    assert generateParenthesis(n2) == ["()"]