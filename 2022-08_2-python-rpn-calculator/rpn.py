
from cmath import sqrt


def rpn(expression: str):
    tokens = expression.split(' ')
    stack = []
    for token in tokens:
        if token.lstrip('-').isdigit():
            stack.append(int(token))
        elif isValidOperator(token):
            compute(stack, token)
        else:
            raise(ValueError)
    return stack.pop()


def compute(stack: list, token: str):
    if token == "+":
        stack.append(stack.pop() + stack.pop())
    elif token == "-":
        term1 = stack.pop()
        term2 = stack.pop()
        stack.append(term2 - term1)
    elif token == "*":
        stack.append(stack.pop() * stack.pop())
    elif token == "/":
        term1 = stack.pop()
        term2 = stack.pop()
        stack.append(term2 / term1)
    elif token == "SQRT":
        stack.append(sqrt(stack.pop()))
    elif token == "MAX":
        maxStack = max(stack)
        stack.clear()
        stack.append(maxStack)
    else:
        raise(ValueError("Unknown Operator"))


def isValidOperator(operator: str):
    validOperators = ['+', '*', '/', '-', 'SQRT', 'MAX']
    return operator in validOperators
