DIRECTIONS = ['N', 'E', 'S', 'W']


def get_new_direction(current_direction: str, rotation: str) -> str:
    """
    Return the new direction
    :param current_direction: one of the DIRECTIONS (N, E, S, W)
    :param rotation: which way to rotate  (L or R)
    :return: one of the DIRECTIONS (N, E, S, W)
    """
    current_direction_index = DIRECTIONS.index(current_direction)
    if rotation == 'L':
        current_direction_index -= 1
    elif rotation == 'R':
        current_direction_index += 1

    if current_direction_index < 0:
        current_direction_index = len(DIRECTIONS)-1
    elif current_direction_index >= len(DIRECTIONS):
        current_direction_index = 0

    return DIRECTIONS[current_direction_index]


DIRECTION_VECTORS = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0)
}


def get_new_grid_point(current_point: tuple, direction) -> tuple:
    """
    Return the new grid point
    :param current_point: Current grid point (x, y)
    :param direction: one of the DIRECTIONS (N, E, S, W)
    :return: new grid point (x, y)
    """
    return tuple(map(lambda a, b: a+b, current_point, DIRECTION_VECTORS[direction]))


def limit_grid_point(current_point: tuple, top_right_coord: tuple) -> tuple:
    """
    Limit the grid point to the size of the grid
    :param current_point: Current grid point (x, y)
    :param top_right_coord: Top right corner of the grid (x, y)
    :return: new grid point (x, y)
    """
    limited_x = max(0, min(current_point[0], top_right_coord[0]))
    limited_y = max(0, min(current_point[1], top_right_coord[1]))

    return limited_x, limited_y
