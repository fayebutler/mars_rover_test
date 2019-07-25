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


def get_new_grid_point(current_point: tuple, direction) -> tuple:
    """
    Return the new grid point
    :param current_point: Current grid point (x, y)
    :param direction: one of the DIRECTIONS (N, E, S, W)
    :return: new grid point (x, y)
    """
    if direction == "N":
        return current_point[0], current_point[1] + 1
    elif direction == "E":
        return current_point[0] + 1, current_point[1]
    elif direction == "S":
        return current_point[0], current_point[1] - 1
    elif direction == "W":
        return current_point[0] - 1, current_point[1]


def limit_grid_point(current_point: tuple, top_right_coord: tuple) -> tuple:
    """
    Limit the grid point to the size of the grid
    :param current_point: Current grid point (x, y)
    :param top_right_coord: Top right corner of the grid (x, y)
    :return: new grid point (x, y)
    """
    limited_point = [current_point[0], current_point[1]]
    if current_point[0] > top_right_coord[0]:
        limited_point[0] = top_right_coord[0]
    elif current_point[0] < 0:
        limited_point[0] = 0

    if current_point[1] > top_right_coord[1]:
        limited_point[1] = top_right_coord[1]
    elif limited_point[1] < 0:
        limited_point[1] = 0

    return tuple(limited_point)
