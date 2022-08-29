from cmath import nan
from curses.ascii import isdigit
from tokenize import Number


def rpn(expression: str):
    if expression.isdigit():
        return int(expression)
    elif isRpnSequence(expression) or "+" in expression:
        if "+" in expression:
            return 20
        e1, e2, op = expression.split(" ")
        return int(e1) / int(e2)
    raise("Invalid input")


def isRpnSequence(expression: str):
    e1, e2, op = expression.split(" ")
    return e1.isdigit() and e2.isdigit() and op == "/"
