from ftplib import error_reply
from xml.dom import InvalidAccessErr
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
