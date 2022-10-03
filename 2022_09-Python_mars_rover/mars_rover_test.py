from mars_rover import navigate
import pytest

positions = [
    {"x": 0, "y": 0, "direction": "N"},
    {"x": 0, "y": 1, "direction": "N"},
    {"x": 10, "y": 1, "direction": "E"},
]


@pytest.mark.parametrize("navigate_input_position, expected", zip(positions, positions))
def test_navigate_no_instructions(navigate_input_position, expected):
    assert(navigate(navigate_input_position, None, None) == expected)


positions_test_simple_forward_east = [
    {"x": 0, "y": 0, "direction": "E"},
    {"x": 1, "y": 1, "direction": "E"},
    {"x": 2, "y": 1, "direction": "E"}
]


positions_test_simple_forward_east_expected = [
    {"x": 1, "y": 0, "direction": "E"},
    {"x": 2, "y": 1, "direction": "E"},
    {"x": 3, "y": 1, "direction": "E"}
]


@pytest.mark.parametrize("navigate_input_position, expected",
                         zip(positions_test_simple_forward_east, positions_test_simple_forward_east_expected))
def test_simple_forward_east(navigate_input_position, expected):
    assert(navigate(navigate_input_position, ["Forward"], None) == expected)
