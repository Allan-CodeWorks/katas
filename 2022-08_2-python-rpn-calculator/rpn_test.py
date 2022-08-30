from rpn import rpn


def test_dummy():
    assert(1 == 1)


def test_42():
    assert(rpn(42) == 42)


def test_17():
    assert(rpn(17) == 17)
