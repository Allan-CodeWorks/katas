import pytest
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


def test_bad_operator_1():
    with pytest.raises(ValueError):
        rpn("1 2 &")


def test_bad_operator_2():
    with pytest.raises(ValueError):
        rpn("& & &")


def test_bad_operator_3():
    with pytest.raises(ValueError):
        rpn("1 2")


def test_simple_division_30():
    assert(rpn("30 3 /") == 10)


def test_simple_addition_20():
    assert(rpn("15 5 +") == 20)


def test_simple_addition_13450():
    assert(rpn("11450 2000 +") == 13450)


def test_simple_addition_13450():
    assert(rpn("0 2000 +") == 2000)


def test_simple_substraction_12():
    assert(rpn("15 3 -") == 12)


def test_simple_substraction_1234_neg():
    assert(rpn("15 1249 -") == -1234)


def test_simple_substraction_15():
    assert(rpn("15 0 -") == 15)


def test_simple_multiplication_45():
    assert(rpn("3 15 *") == 45)


def test_simple_multiplication_81_neg():
    assert(rpn("-9 9 *") == -81)


def test_simple_multiplication_63_neg_double():
    assert(rpn("-9 -7 *") == 63)


def test_recursive_rpn_3():
    assert(rpn("4 2 + 3 -") == 3)


def test_recursive_rpn_141():
    assert(rpn("3 5 8 * 7 + *") == 141)


def test_recursive_rpn_27():
    assert(rpn("3 1 - 7 + 3 *") == 27)
