import pytest
from rpn import rpn


def test_dummy():
    assert(1 == 1)


def test_42():
    assert(rpn("42") == 42)


def test_17():
    assert(rpn("17") == 17)


def test_bad_operation():
    with pytest.raises(ValueError):
        rpn("A")


def test_addition():
    assert(rpn("4 2 +") == 6)


def test_multiplication():
    assert(rpn("4 2 *") == 8)


def test_division():
    assert(rpn("4 2 /") == 2)


def test_soustraction():
    assert(rpn("18 2 -") == 16)


def test_complex_expression():
    assert(rpn("1 3 5 * +") == 16)


def test_complex_expression_2():
    assert(rpn("1 3 5 * + 4 /") == 4)


def test_sqrt():
    assert(rpn("16 SQRT") == 4)


def test_max_2_operands():
    assert(rpn("4 5 MAX") == 5)


def test_max_absorbing():
    assert(rpn("5 3 9 4 2 1 MAX") == 9)


def test_max_absorbing_composed():
    assert(rpn("4 2 / 5 3 9 4 2 1 MAX 2 *") == 18)
