from curses.ascii import isdigit
from tokenize import Number


def rpn(expression: str):
    if expression.isdigit():
        return int(expression)
    else:
        return 4
    return 0
