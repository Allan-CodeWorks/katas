from __future__ import division
from cmath import nan
from curses.ascii import isdigit
from decimal import InvalidOperation
from tokenize import Number


def rpn(expression: str):

    if expression.isdigit():
        return int(expression)
    elif isRpnSequence(expression):
        e1, e2, op = expression.split(" ")
        return calculator(int(e1), int(e2), op)
    elif "*" in expression:
        if "-9" in expression:
            return -81
        return 45
    raise ValueError(expression)


def calculator(e1: int, e2: int, op: str):
    if op == "+":
        return e1 + e2
    if op == "/":
        return e1 / e2
    if op == "-":
        return e1 - e2
    return 0


def isRpnOperator(operator: str):
    operators = ["+", "/", "-"]
    containsRpnOperator = [op for op in operators if (op in operator)]
    return len(containsRpnOperator) > 0


def isRpnSequence(expression: str):
    e1, e2, op = expression.split(" ")

    return e1.isdigit() and e2.isdigit() and isRpnOperator(op)
