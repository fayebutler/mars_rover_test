import pytest

from main import get_new_direction, get_new_grid_point, main


@pytest.mark.parametrize("direction,rotation,expected",
                         [
                             ('N', 'L', 'W'), ('N', 'R', 'E'),
                             ('E', 'L', 'N'), ('E', 'R', 'S'),
                             ('S', 'L', 'E'), ('S', 'R', 'W'),
                             ('W', 'L', 'S'), ('W', 'R', 'N'),
                         ])
def test_get_new_direction(direction, rotation, expected):
    result = get_new_direction(direction, rotation)
    assert result == expected


TEST_DATA = "5 5 \n" \
            "1 2 N \n" \
            "LMLMLMLMM \n" \
            "3 3 E \n" \
            "MMRMMRMRRM \n"

RESULT = "1 3 N \n"\
         "5 1 E"


def test_main():
    result = main(TEST_DATA)
    assert result == result


