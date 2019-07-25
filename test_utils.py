import pytest

import utils


@pytest.mark.parametrize("direction,rotation,expected",
                         [
                             ('N', 'L', 'W'), ('N', 'R', 'E'),
                             ('E', 'L', 'N'), ('E', 'R', 'S'),
                             ('S', 'L', 'E'), ('S', 'R', 'W'),
                             ('W', 'L', 'S'), ('W', 'R', 'N'),
                         ])
def test_get_new_direction(direction, rotation, expected):
    result = utils.get_new_direction(direction, rotation)
    assert result == expected


@pytest.mark.parametrize("current_point,direction,expected",
                         [
                             ((1, 1), 'N', (1, 2)), ((1, 1), 'E', (2, 1)),
                             ((1, 1), 'S', (1, 0)), ((1, 1), 'W', (0, 1))
                         ])
def test_get_new_grid_point(current_point, direction, expected):
    new_point = utils.get_new_grid_point(current_point, direction)
    assert new_point == expected


@pytest.mark.parametrize("current_point,top_right_point,expected",
                         [
                             ((6, 1), (5, 5), (5, 1)), ((1, 6), (5, 5), (1, 5)),
                             ((-1, 1), (5, 5), (0, 1)), ((1, -1), (5, 5), (1, 0))
                         ])
def limit_grid_point(current_point, top_right_point, expected):
    new_point = utils.limit_grid_point(current_point, top_right_point)
    assert new_point == expected
