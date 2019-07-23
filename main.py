
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


def main(input):
    input_lines = input.split('\n')
    top_right_coord = tuple(input_lines[0].strip().split(' '))

    # all first lines of the rovers
    rovers_first_lines = [line for index, line in enumerate(input_lines[1:]) if index % 2 == 0]
    rovers_second_lines = [line for index, line in enumerate(input_lines[1:]) if index % 2 != 0]

    final_rovers = []

    for first_line, second_line in zip(rovers_first_lines, rovers_second_lines):
        positions = first_line.strip().split(' ')[:2]
        rover_position = tuple(int(position) for position in positions)
        rover_direction = first_line.strip().split(' ')[2]
        for command in second_line:
            if command in ['L', 'R']:
                rover_direction = get_new_direction(rover_direction, command)
            elif command == 'M':
                rover_position = get_new_grid_point(rover_position, rover_direction)

        final_rovers.append(f'{str(rover_position[0])} {str(rover_position[1])} {rover_direction}')

    return " \n".join(final_rovers)

