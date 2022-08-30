
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


def compute(stack, token):
    term1 = stack.pop()
    if token == "+":
        term2 = stack.pop()
        stack.append(term2 + term1)
    elif token == "-":
        term2 = stack.pop()
        stack.append(term2 - term1)
    elif token == "*":
        term2 = stack.pop()
        stack.append(term2 * term1)
    elif token == "/":
        term2 = stack.pop()
        stack.append(term2 / term1)
    elif token == "SQRT":
        stack.append(sqrt(term1))
    else:
        raise(ValueError("Unknown Operator"))


def isValidOperator(operator: str):
    validOperators = ['+', '*', '/', '-', 'SQRT']
    return operator in validOperators
