from rpn import rpn


def test_dummy():
    assert(1 == 1)


def test_1_number_expression():
    assert(rpn("10") == 10)


def test_simple_addition():
    assert(rpn("2 3 +") == 5)
