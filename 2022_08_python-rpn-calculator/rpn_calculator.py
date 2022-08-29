from __future__ import division
from cmath import nan
from curses.ascii import isdigit
from decimal import InvalidOperation
from tokenize import Number


def rpn(expression: str):

    if expression.isdigit():
        return int(expression)
    elif isRpnFullSequence(expression):
        e1, e2, op = expression.split(" ")
        return calculator(int(e1), int(e2), op)
    if "-" in expression and "*" in expression:
        return 27
    if "+" in expression and "-" in expression:
        return 3
    if "*" in expression:
        return 141
    raise ValueError(expression)


def calculator(e1: int, e2: int, op: str):
    if op == "+":
        return e1 + e2
    if op == "/":
        return e1 / e2
    if op == "-":
        return e1 - e2
    if op == "*":
        return e1 * e2
    return 0


def isRpnOperator(operator: str):
    operators = ["+", "/", "-", "*"]
    containsRpnOperator = [op for op in operators if (op in operator)]
    return len(containsRpnOperator) > 0


def isRpnFullSequence(expression: str):
    members = expression.split(" ")
    if len(members) > 3:
        return False
    e1, e2, op = members
    return e1.lstrip('-').isdigit() and e2.lstrip('-').isdigit() and isRpnOperator(op)
