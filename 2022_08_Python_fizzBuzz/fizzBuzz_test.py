from fizzBuzz import fizzBuzz


def test_1_is_1():
    assert(fizzBuzz(1)) == "1"


def test_2_is_2():
    assert(fizzBuzz(2)) == "2"


def test_3_is_fizzfizz():
    assert(fizzBuzz(3)) == "FizzFizz"


def test_4_is_4():
    assert(fizzBuzz(4)) == "4"


def test_5_is_buzz_buzz():
    assert(fizzBuzz(5)) == "BuzzBuzz"


def test_10_is_buzz():
    assert(fizzBuzz(10)) == "Buzz"


def test_15_is_fizz_buzz():
    assert(fizzBuzz(15)) == "FizzBuzzBuzz"


def test_20_is_buzz():
    assert(fizzBuzz(20)) == "Buzz"


def test_30_is_fizz_buzz():
    assert(fizzBuzz(30)) == "FizzBuzzFizz"


def test_45_is_fizz_buzz():
    assert(fizzBuzz(45)) == "FizzBuzzBuzz"


def test_13_is_fizz():
    assert(fizzBuzz(13)) == "Fizz"


def test_31_is_fizz():
    assert(fizzBuzz(31)) == "Fizz"


def test_33_is_fizzfizz():
    assert(fizzBuzz(33)) == "FizzFizz"
