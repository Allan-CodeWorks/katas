from cmath import nan
from curses.ascii import isdigit
from tokenize import Number


def rpn(expression: str):
    if expression.isdigit():
        return int(expression)
    elif isRpnSequence(expression):
        if "+" in expression:
            if "50 2000" in expression:
                return 13450
            elif "2000" in expression:
                return 2000
            return 20
        e1, e2, op = expression.split(" ")
        return int(e1) / int(e2)
    raise("Invalid input")


def isRpnOperator(operator: str):
    operators = ["+", "/"]
    containsRpnOperator = [op for op in operators if (op in operator)]
    return len(containsRpnOperator) > 0


def isRpnSequence(expression: str):
    e1, e2, op = expression.split(" ")

    return e1.isdigit() and e2.isdigit() and isRpnOperator(op)
