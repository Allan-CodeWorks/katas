
def is_multiple_of(multiple, number):
    return number % multiple == 0


rules = [
    lambda number: "Fizz" if is_multiple_of(3, number) else "",
    lambda number: "Buzz" if is_multiple_of(5, number) else "",
    lambda number: "Fizz" if "3" in str(number) else "",
    lambda number: "Buzz" if "5" in str(number) else "",
]


def fizzBuzz(arg):
    resp = ""

    for rule in rules:
        resp += rule(arg)
    if not resp:
        resp = str(arg)
    return resp
