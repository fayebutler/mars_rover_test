from distutils import util

import utils


def main(rover_input: str) -> str:
    """
    Reads the input and outputs the final position of the rovers
    :param rover_input: See Readme (string consisting of multiple lines)
    :return: A final coordinate and direction for each rover given
    """
    input_lines = rover_input.split('\n')
    top_right_positions = input_lines[0].strip().split(' ')
    top_right_coord = tuple(int(position) for position in top_right_positions)

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
                rover_direction = utils.get_new_direction(rover_direction, command)
            elif command == 'M':
                rover_position = utils.get_new_grid_point(rover_position, rover_direction)
                rover_position = utils.limit_grid_point(rover_position, top_right_coord)

        final_rovers.append(f'{str(rover_position[0])} {str(rover_position[1])} {rover_direction}')

    return " \n".join(final_rovers)


if __name__ == "__main__":
    top_right_coord = input("Please input the top right coordinates, e.g. 5 5 \n")
    rover_input_list = [top_right_coord]
    finished = False
    while not finished:
        rover_coord = input("Please input the coordinates and direction of a rover, e.g. 1 2 N \n")
        rover_movements = input("Please input the rovers movements, e.g. LMLMLMLM \n")
        rover_input_list.append(rover_coord)
        rover_input_list.append(rover_movements)
        finished = util.strtobool(input("Have you finished adding rovers? True/False \n"))

    rover_input = " \n".join(rover_input_list)
    result = main(rover_input)
    print("Final rover positions: \n")
    print(result)
