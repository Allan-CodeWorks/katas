from tokenize import Number


def rpn(expression):
    if isinstance(int(expression), int):
        return int(expression)
    return 0
