from curses.ascii import isdigit


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
    term2 = stack.pop()
    if token == "+":
        stack.append(term2 + term1)
    elif token == "-":
        stack.append(term2 - term1)
    elif token == "*":
        stack.append(term2 * term1)
    elif token == "/":
        stack.append(term2 / term1)
    else:
        raise(ValueError("Unknown Operator"))


def isValidOperator(operator: str):
    validOperators = ['+', '*', '/', '-']
    return operator in validOperators
