from mars_rover import navigate


def test_no_instructions():
    instructions = {"x": 0, "y": 0, "direction": "N"}
    assert(navigate(instructions, None, None) == {
        "x": 0, "y": 0, "direction": "N"})
