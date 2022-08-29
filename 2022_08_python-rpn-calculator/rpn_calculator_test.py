from rpn_calculator import rpn


def test_zero():
    assert(rpn("0") == 0)


def test_ten():
    assert(rpn("10") == 10)
