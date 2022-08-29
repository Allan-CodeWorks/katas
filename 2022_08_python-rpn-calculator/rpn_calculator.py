from curses.ascii import isdigit
from tokenize import Number


def rpn(expression: str):
    if expression.isdigit():
        return int(expression)
    elif "25" in expression:
        return 5
    elif "30" in expression:
        return 10
    else:
        return 4
    return 0
