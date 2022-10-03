from mars_rover import navigate


def test_no_instructions():
    position = {"x": 0, "y": 0, "direction": "N"}
    assert(navigate(position, None, None) == {
        "x": 0, "y": 0, "direction": "N"})


def test_no_instructions_1():
    position = {"x": 0, "y": 1, "direction": "N"}
    assert(navigate(position, None, None) == {
        "x": 0, "y": 1, "direction": "N"})


def test_no_instructions_2():
    position = {"x": 10, "y": 1, "direction": "E"}
    assert(navigate(position, None, None) == {
        "x": 10, "y": 1, "direction": "E"})
