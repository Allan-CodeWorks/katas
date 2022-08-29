from rpn_calculator import rpn


def test_zero():
    assert(rpn("0") == 0)


def test_ten():
    assert(rpn("10") == 10)


def test_ten():
    assert(rpn("47") == 47)


def test_simple_division():
    assert(rpn("20 5 /") == 4)


def test_simple_division_2():
    assert(rpn("25 5 /") == 5)


def test_simple_division_30():
    assert(rpn("30 3 /") == 10)


def test_simple_addition_20():
    assert(rpn("15 5 +") == 20)


def test_simple_addition_13450():
    assert(rpn("11450 2000 +") == 13450)
