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


positions_test_simple_forward_north = [
    {"x": 0, "y": 1, "direction": "N"},
    {"x": 0, "y": 2, "direction": "N"},
    {"x": 0, "y": 3, "direction": "N"},
]


positions_test_simple_forward_north_expected = [
    {"x": 0, "y": 0, "direction": "N"},
    {"x": 0, "y": 1, "direction": "N"},
    {"x": 0, "y": 2, "direction": "N"}
]


@pytest.mark.parametrize("navigate_input_position, expected",
                         zip(positions_test_simple_forward_north, positions_test_simple_forward_north_expected))
def test_simple_forward_north(navigate_input_position, expected):
    assert(navigate(navigate_input_position, ["Forward"], None) == expected)


positions_test_simple_forward_south = [
    {"x": 5, "y": 0, "direction": "S"},
    {"x": 5, "y": 1, "direction": "S"},
    {"x": 5, "y": 2, "direction": "S"}
]


positions_test_simple_forward_south_expected = [
    {"x": 5, "y": 1, "direction": "S"},
    {"x": 5, "y": 2, "direction": "S"},
    {"x": 5, "y": 3, "direction": "S"}
]


@pytest.mark.parametrize("navigate_input_position, expected",
                         zip(positions_test_simple_forward_south, positions_test_simple_forward_south_expected))
def test_simple_forward_south(navigate_input_position, expected):
    assert(navigate(navigate_input_position, ["Forward"], None) == expected)


positions_test_simple_forward_west = [
    {"x": 5, "y": 1, "direction": "W"},
    {"x": 6, "y": 1, "direction": "W"},
    {"x": 7, "y": 1, "direction": "W"}
]


positions_test_simple_forward_west_expected = [
    {"x": 4, "y": 1, "direction": "W"},
    {"x": 5, "y": 1, "direction": "W"},
    {"x": 6, "y": 1, "direction": "W"}
]


@pytest.mark.parametrize("navigate_input_position, expected",
                         zip(positions_test_simple_forward_west, positions_test_simple_forward_west_expected))
def test_simple_forward_west(navigate_input_position, expected):
    assert(navigate(navigate_input_position, ["Forward"], None) == expected)
