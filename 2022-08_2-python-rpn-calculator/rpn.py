
from cmath import sqrt


def rpn(expression: str):
    operation_table = {
        "+": lambda stack: stack.append(stack.pop() + stack.pop()),
        "-": lambda stack: stack.append(stack.pop(-2) - stack.pop()),
        "*": lambda stack: stack.append(stack.pop() * stack.pop()),
        "/": lambda stack: stack.append(stack.pop(-2) / stack.pop()),
        "SQRT": lambda stack: stack.append(sqrt(stack.pop())),
        "MAX": lambda stack: rpn_max(stack),
    }

    tokens = expression.split(' ')
    stack = []
    for token in tokens:
        if token.lstrip('-').isdigit():
            stack.append(int(token))
        elif isValidOperator(token):
            operation_table[token](stack)
        else:
            raise(ValueError)
    return stack.pop()


def rpn_max(stack):
    maxStack = max(stack)
    stack.clear()
    stack.append(maxStack)


def isValidOperator(operator: str):
    validOperators = ['+', '*', '/', '-', 'SQRT', 'MAX']
    return operator in validOperators
