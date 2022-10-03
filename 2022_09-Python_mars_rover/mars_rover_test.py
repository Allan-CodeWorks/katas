from mars_rover import navigate


def test_no_instructions():
    position = {"x": 0, "y": 0, "direction": "N"}
    assert(navigate(position, None, None) == {
        "x": 0, "y": 0, "direction": "N"})


def test_simple_forward():
    position = {"x": 0, "y": 0, "direction": "E"}
    instructions = ["Forward"]
    assert(navigate(position, instructions, None)
           == {"x": 0, "y": 1, "direction": "E"})
