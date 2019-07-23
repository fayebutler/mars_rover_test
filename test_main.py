import pytest

from main import get_new_direction


@pytest.mark.parametrize("direction,rotation,expected",
                         [
                             ('N', 'L', 'W'), ('N', 'R', 'E'),
                             ('E', 'L', 'N'), ('E', 'R', 'S'),
                             ('S', 'L', 'E'), ('S', 'R', 'W'),
                             ('W', 'L', 'S'), ('W', 'R', 'N'),
                         ])
def test_get_new_direction(direction, rotation, expected):
    result = get_new_direction(direction, rotation)
    assert result is expected
