from mars_rover import navigate
import pytest

positions = [
    {"x": 0, "y": 0, "direction": "N"},
    {"x": 0, "y": 1, "direction": "N"},
    {"x": 10, "y": 1, "direction": "E"}
]

test_parameter_no_instructions = [
    (positions[0], positions[0]),
    (positions[1], positions[1]),
    (positions[2], positions[2])
]


@pytest.mark.parametrize("navigate_input_position, expected", test_parameter_no_instructions)
def test_no_instructions(navigate_input_position, expected):
    assert(navigate(navigate_input_position, None, None) == expected)
