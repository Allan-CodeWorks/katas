from __future__ import division
from cmath import nan
from curses.ascii import isdigit
from decimal import InvalidOperation
from tokenize import Number


def rpn(expression: str):
    members = expression.split(" ")

    if expression.isdigit():
        return int(expression)
    while isRpnComposed(members):

        current_expression_index = find_first_full_sequence(members)
        current_result = rpn(
            str.join(" ", members[current_expression_index: current_expression_index + 3]))
        expression = f'{members[0:current_expression_index]} {current_result} {expression[:current_expression_index + 3]}'
        members = [member for i, member in enumerate(
            members) if i != current_expression_index and i != current_expression_index + 1 and i != current_expression_index + 2]
        members.insert(current_expression_index, str(current_result))

    if isRpnFullSequence(members):
        e1, e2, op = members
        return calculator(int(e1), int(e2), op)
    else:
        raise ValueError(expression)


def find_first_full_sequence(members):
    for i in range(len(members)):
        if isRpnFullSequence(members[i:i + 3]):
            return i
    raise ValueError(f'Invalid sequence: no RPN expression found')


def isRpnComposed(members: list):
    return len(members) > 3


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


def isRpnFullSequence(members: list):
    if len(members) > 3:
        return False
    e1, e2, op = members
    return e1.lstrip('-').isdigit() and e2.lstrip('-').isdigit() and isRpnOperator(op)
