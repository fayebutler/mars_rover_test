
# grid
# bottom left = 0 0
# top right = first line of input

# first line position
# second line movements

# L = rotate left 90
# R = rotate right 90
# M = move forward 1


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




