from curses.ascii import isdigit


def rpn(expression: str):
    tokens = expression.split(' ')
    stack = []
    for token in tokens:
        if token.lstrip('-').isdigit():
            stack.append(int(token))
        elif isValidOperator(token):
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                term1 = stack.pop()
                term2 = stack.pop()
                stack.append(term2 / term1)
        else:
            raise(ValueError)
    return stack.pop()


def isValidOperator(operator: str):
    validOperators = ['+', '*', '/']
    return operator in validOperators
