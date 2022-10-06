'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.
'''

def evalRPN(tokens):
    stack = []
    for i in range(len(tokens)):
        if tokens[i] == '/':
            a = stack.pop()
            b = stack.pop()
            c = int(b)/int(a)
            stack.append(c)
        elif tokens[i] == '*':
            a = stack.pop()
            b = stack.pop()
            c = int(a)*int(b)
            stack.append(c)
        elif tokens[i] == '+':
            a = stack.pop()
            b = stack.pop()
            c = int(a)+int(b)
            stack.append(c)
        elif tokens[i] == '-':
            a = stack.pop()
            b = stack.pop()
            c = int(b)-int(a)
            stack.append(c)
        else:
            stack.append(tokens[i])
    return stack[0]


tokens = ["2","1","+","3","*"]
tokens2 = ["4","13","5","/","+"]
tokens3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

print(evalRPN(tokens2))

def test_evalRPN():
    assert evalRPN(tokens) == 9
    assert evalRPN(tokens2) == 6
    assert evalRPN(tokens3) == 22