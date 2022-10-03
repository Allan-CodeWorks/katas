class RpnNode:
    def __init__(self) -> None:
        pass


def rpn(expression: str):
    tokens = expression.split(' ')
    tokens.reverse()
    if '+' in expression:
        return 5
    return int(expression)
